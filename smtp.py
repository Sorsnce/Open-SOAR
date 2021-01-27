def smtp(sender=None, receiver=None, password=None, smtp_server=None, html=None, subject=None, **kwargs):
    """
        The following code with take the fields passed to the function to create an email

        Returns a JSON-serializable object that implements the configured data paths:

    """
    import smtplib
    import ssl
    import json
    from email.mime.text import MIMEText

    sender = sender
    receivers = [receiver]

    port = 465
    user = sender
    password = password

    #msg = MIMEText('This is test mail')
    html = html
    msg = MIMEText(html, "html")
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = receiver

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(user, password)
        server.sendmail(sender, receivers, msg.as_string())
        print('mail successfully sent')

    outputs = {}

    # Write your custom code here...

    # Return a JSON-serializable object
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs
