def cyber_daily(imap_server=None, username=None, password=None, folder_id=None, **kwargs):
    import email
    import imaplib
    import json
    import re

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
