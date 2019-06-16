# Argos Raspberry

Project in python to perform http requests and actions on google drive for the cloud from the raspberry.

## execute script

launched sensor script :
<pre>
<code>
make sensor
</pre>
</code>

launched action script :
<pre>
<code>
make action
</code>
</pre>

## Create Service file

- create a service file :
<pre>
<code>
sudo vim/nano /lib/systemd/system/your_service.service
</code>
</pre>

- add the following content in it, change just the description and the Execstart :
<pre>
<code>
[Unit]
Description=Your_Name_Service
After=multi-user.target
Conflicts=getty@tty1.service

[Service]
Type=simple
ExecStart=/usr/bin/python3 /path/to/project/your_python_file.py #main.py
StandardInput=tty-force

[Install]
WantedBy=multi-user.target
</code>
</pre>

- Enable newly added service
<pre>
<code>
sudo systemctl daemon-reload
sudo systemctl enable your_service.service
sudo systemctl start your_service.service
</code>
</pre>

## Create log file

add in service file, below of StandardInput this line :
<pre>
<code>
StandardOutput=syslog
StandardError=syslog
SyslogIdentifier=your_identifier # example : argosraspberry
</code>
</pre>

- create a file in /etc/rsyslog.d/name_file.conf with the following content:
<pre>
<code>
if $programname == 'your_identifier' then /path/to/log/your_file.log
& stop
</pre>
</code>

- After it, change the permissions of that path to something readable by syslog:
<pre>
<code>
# ls -alth /var/log/syslog 
-rw-r----- 1 root adm 439K Mar  5 19:35 /var/log/syslog
# chown root:adm /path/to/log/your_file.log
</code>
</pre>

- restart all :
<pre>
<code>
sudo systemctl restart rsyslog
sudo systemctl daemon-reload
sudo systemctl restart your_service.service
</code>
</pre>
