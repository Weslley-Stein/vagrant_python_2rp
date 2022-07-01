import os

def main():
    os.system("yum install -y java-11-openjdk-devel && export JAVA_HOME=$(readlink -f $(which java)) && export JRE_HOME=$(readlink -f $(which java)/jre)")
    os.system("export JAVA_HOME=$(readlink -f $(which java))")
    os.system("export JRE_HOME=$(readlink -f $(which java)/jre)")
    os.system("yum install -y wget")
    os.system("wget --no-check-certificate https://dlcdn.apache.org/zeppelin/zeppelin-0.10.1/zeppelin-0.10.1-bin-all.tgz && tar xvf zeppelin-*-bin-all.tgz -C /opt")
    os.makedirs("/opt/zeppelin")
    os.system("mv /opt/zeppelin-*-bin-all/* /opt/zeppelin"
    os.system("adduser -d /opt/zeppelin -s /sbin/nologin zeppelin")
    os.system("chown -R zeppelin:zeppelin /opt/zeppelin")
    os.chdir("/etc/systemd/system")
    os.system("touch zeppelin.service")
    os.system('''echo -e "
[Unit]\n\
Description=Zeppelin service\n
After=syslog.target network.target\n\
[Service]\n
Type=forking\n
ExecStart=/opt/zeppelin/bin/zeppelin-daemon.sh start\n
ExecStop=/opt/zeppelin/bin/zeppelin-daemon.sh stop\n
ExecReload=/opt/zeppelin/bin/zeppelin-daemon.sh reload\n
User=zeppelin\n
Group=zeppelin\n
Restart=always\n\
[Install]\n
WantedBy=multi-user.target" >> zeppelin.service''')
    os.system("systemctl start zeppelin && systemctl enable zeppelin")
    os.system("yum install -y epel-release")
    os.system("yum install -y nginx && systemctl start nginx && systemctl enable nginx")

main()
    
