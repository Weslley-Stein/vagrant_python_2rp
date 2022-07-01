# Step 1
```bash
export VAGRANT_EXPERIMENTAL="disks"
vagrant plugin install vagrant-disksize
```

# Step 2
```bash
vagrant up tworp

vagrant ssh tworp

#Dentro da VM
sudo passwd root #coloque a senha como "tworp123"

su root #Coloca o password que definiu

yum update -y

yum install python3 -y

sudo python3 script.py 
```


