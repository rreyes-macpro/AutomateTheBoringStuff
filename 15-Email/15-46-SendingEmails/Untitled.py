import smtplib

esender = 'monstermon1972@gmail.com'
ereceiver = 'ramongreyes@icloud.com'
ebody = 'Subject : Kulafu\n\nDear Pogi, \nI got you. \n\n - MonPogi'
epwd = 'Eskimo72'

conn = smtplib.SMTP('smtp.gmail.com',587)
type(conn)
conn
conn.ehlo()
conn.starttls()
conn.login(esender, epwd)
conn.sendmail(esender, ereceiver, ebody)
{}
conn.quit()

