# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.define "tworp" do |tworp|
    tworp.vm.box = "centos/7"
    tworp.disksize.size = "50GB"
    tworp.vm.provider "virtualbox" do |vb|
      vb.cpus = 2
      vb.memory = 4096
      vb.name = "teste-zeppelin"
    end
  end
end

