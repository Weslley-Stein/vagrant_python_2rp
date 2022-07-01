# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.define "tworp" do |tworp|
    tworp.vm.box = "centos/7"
    tworp.disksize.size = "50GB"
    tworp.vm.network "public_network", ip:"192.168.0.50"
    #tworp.vm.network "forwarded_port", guest: 80, host: 80, guest_ip: "127.0.0.1", host_ip: "127.0.0.1"
    tworp.vm.provision "file" , source: "./script.py", destination: "$HOME/script.py"
    tworp.vm.provider "virtualbox" do |vb|
      vb.cpus = 2
      vb.memory = 4096
      vb.name = "teste-zeppelin"
    end
  end
end

