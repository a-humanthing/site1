import cgi
form = cgi.FieldStorage()
if metho
resname = form.getvalue('name')
resemail = form.getvalue('email')
ressub = form.getvalue('subject')
resmessage = form.getvalue('message')
print(resname,resemail,ressub,resmessage)