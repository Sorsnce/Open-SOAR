def cyber_daily(imap_server=None, username=None, password=None, folder_id=None, **kwargs):
    """
    This app is designed to take email threat Intel and parse CVE data as well as external IP data from an imap server. We currently only support Intel via O365 via Recorded Future's CyberDaily email feed.
    
    Args:
        imap_server (CEF type: ip): This will be the IP or DNS of the imap server. We currently only support O365
        username (CEF type: username): This will be the username you use to sign into the mailbox. We currently only support O365
        password (CEF type: password): This will be the password you use to sign into the mailbox. We currently only support O365
        folder_id: This will be the name of the folder you want to ingest email to look for CVEs and IP address.
    
    Returns a JSON-serializable object that implements the configured data paths:
        cve (CEF type: cve): This will be a list of CVEs parsed from the threat Intel email
        ip (CEF type: ip): This will be a list of IPs parsed from the threat Intel email
    """

    import email
    import imaplib
    import json
    import re
    # Uncomment this if you want to use this code in Splunk>Phantom custom function
    #import phantom.rules as phantom

    mail = imaplib.IMAP4_SSL(imap_server)
    mail.login(username, password)
    mail.select(folder_id)

    status, data = mail.search(None, 'UNSEEN')

    mail_ids = []

    for block in data:
        mail_ids += block.split()

    for i in mail_ids:
        status, data = mail.fetch(i, '(RFC822)')
        for response_part in data:
            if isinstance(response_part, tuple):
                message = email.message_from_bytes(response_part[1])
                mail_from = message['from']
                mail_subject = message['subject']
                if message.is_multipart():
                    mail_content = ''
                    for part in message.get_payload():
                        if part.get_content_type() == 'text/plain':
                            mail_content += part.get_payload()
                else:
                    mail_content = message.get_payload()
                # print(f'From: {mail_from}')
                # print(f'Subject: {mail_subject}')
                data = mail_content
                # print(type(mail_content))
    try:
        cve = re.findall(r'[^\(|^\[](CVE-.*?-.*?)\s', data)
        ip_unfilter = re.findall(r'(\d+\[\.\].*?\[\.\].*?\[\.\].*?)\s', data)

        def fix(x):
            return x.replace('[', '').replace(']', '')

        result = map(fix, ip_unfilter)
        ip = list(result)
        outputs = {
            'cve': cve,
            'ip': ip
        }
        assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
        return outputs

    except:
        error = "No new Cyber Daily Emails in inbox"
        return error