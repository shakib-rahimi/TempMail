class TempMail:
  url_gen = r"https://www.1secmail.com/api/v1/"
  def __init__(self, count=1):
    self.mails=self.generate_new_random_mails(count)

  def generate_new_random_mails(self, count:int=1)->list:
    self.mails=requests.get(self.url_gen,params={'action':'genRandomMailbox','count':count}).json()
    return self.mails
  
  def get_messages(self, mail_inx):
    login, domain = self.mails[mail_inx].split('@')
    return requests.get(self.url_gen,params={'action':'getMessages','login':login, 'domain':domain}).json()
  
  def read_message(self, mail_inx, message_id):
    login, domain = self.mails[mail_inx].split('@')
    return requests.get(self.url_gen,params={'action':'readMessage','login':login, 'domain':domain, 'id':message_id}).json()
  
  def get_all_messages_of_mail(self, mail_inx):
    message_list = self.get_messages(mail_inx)
    return [self.read_message(mail_inx, el['id']) for el in message_list]
  
  def get_all_messages_of_all_mails(self):
    return [self.get_all_messages_of_mail(i) for i in range(len(self.mails))]
