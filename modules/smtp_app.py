def smtp_app(sender=None, receiver=None, password=None, smtp_server=None, html_body=None, subject=None, port=None,
             **kwargs):
    """
    This app will send an HTML formatted SMTP email to the specified values

    Args:
        sender (CEF type: email): This should be the email sender. Depending on the SMTP server you may need 'Send As' access from this email address.
        receiver (CEF type: email): This should be a single or multiple email addresses you want to send the HTML formatted email too.
        password: This should be the password to the account that is "sending" this HTML formatted email.
        smtp_server (CEF type: ip): This should be the IP address or DNS name of the SMTP server. i.e. smtp.yahoo.com
        html_body: This will be a HTML formatted string to use as the body of the email.
        subject: This will be the subject of the email being sent.
        port (CEF type: port): This should be the port used to connect to the SMTP server. i.e. 25 or 465

    Returns a JSON-serializable object that implements the configured data paths:

    """

    import json
    # Uncomment this if you want to use this code in Splunk>Phantom custom function
    # import phantom.rules as phantom
    import smtplib
    import ssl
    from email.mime.text import MIMEText

    sender = sender
    receivers = [receiver]

    user = sender
    password = password

    html = html_body
    msg = MIMEText(html, "html")
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = receiver

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(user, password)
        server.sendmail(sender, receivers, msg.as_string())
        outputs = {'data': 'mail successfully sent'}

    # Return a JSON-serializable object
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs
