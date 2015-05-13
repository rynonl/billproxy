import asyncore
import email
import smtpd

class CustomSMTPServer(smtpd.SMTPServer):
      
  def process_message(self, peer, mailfrom, rcpttos, data):
    print 'Receiving message from:', peer
    print 'Message addressed from:', mailfrom
    print 'Message addressed to  :', rcpttos
    print 'Message length        :', len(data)
    
    parsed = email.message_from_string(data)
    print parsed

    return

server = CustomSMTPServer(('0.0.0.0', 25), None)

asyncore.loop()
