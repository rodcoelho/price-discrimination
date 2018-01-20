## Dotfiles - Create a VPN

#### Step 1 - Setup

Clone the repository: `$ git clone https://github.com/rodcoelho/dotfiles.git`

#### Step 2 - Configure

In `build.py` change the `username` variable in the `mac_pa_token` to your local mac username.

To check your username, open Terminal and type `whoami`

#### Step 3: Spin up your VPN

Run `python3 build.py number_of_vms`

Ex1: `python3 build.py 1` Builds 1 virtual private server

Ex2: `python3 build.py 3` Builds 3 virtual private servers

#### Step 4: Teardown your VPN

`teardown.py` is not production ready. For the time being you will need to log into your digitalocean account and 
manually destroy the clusters you have created. 


####