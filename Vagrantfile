Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/trusty32"
  # make step for openfst failed with memory error. Need swapspace
  config.vm.provision "shell",inline: "sudo apt install swapspace -y"
 # increase memory. without this memory = 512 (megabytes). 
 # not sure of purpose of cpus.
 config.vm.provider "virtualbox" do |v|
   v.memory = 2048 # 4096 
   #v.cpus = 2
 end
  #config.vm.provision "shell", path: "script.sh"
  #config.vm.network :forwarded_port, guest: 4000, host: 8080, host_ip: "127.0.0.1"
end
