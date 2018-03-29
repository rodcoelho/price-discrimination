## Dotfiles for Price Delta Tracker

Dotfile that spins up and configures virtual machines in different geographic locations to find differences in flight prices using Selenium

#### Step 1 - Setup

Clone the repository: `$ git clone https://github.com/rodcoelho/dotfiles.git`

#### Step 2 - SSH keys


If you have SSH keys already, skip to Step 3.

If you do NOT have SSH keys set up (or don't know what they are):

- `$ mkdir .ssh`
- `$ cd .ssh`
- `$ ssh-keygen` and hit enter until a unique 'randomart image' is displayed
- if you type `$ ls -a` you will see that you have two new files created.
- `$ cat id_rsa.pub` At this point you will see a bunch of weird letters and numbers print out. You will need this for the next step.
- PS. `id_rsa.pub` is your public key, it is safe to share your public key. DO NOT SHARE the `id_rsa` file, which is your PRIVATE key.

#### Step 3: Create an account on DigitalOcean.com

Once you have created your digital ocean account, go to the 'Droplets' tab and click 'Create Droplets'. Find 'Add your SSH keys'. 
Here is there you'll paste the weird output from `$ cat id_rsa.pub` you got earlier from your terminal. 

Cool. Now exit digital ocean. We will spin up and configure the rest of our Virtual Machine from the command line.


#### Step 4: Final step before we spin up our VMs

In your terminal, type `$ whoami`. It will show your computer's User name. Mine is `rodrigocoelho`.

In `digitalocean.py` and files within `procedures/` anytime you see `rodrigocoelho`, change it to your computer's User name.


#### Step 5: Spin up the VMs

Before running `$ ./run.sh` go into `shell.py` and comment out line 70. I've added line 70 to send me a text message once the VMs are ready and configured.

Run `$ ./run.sh`.  

The runtime is roughly 2 mins per virtual machine. We are spinning up 4 virtual machines in locations around the US - do the math..

`$ run.sh` does the following: 

- `shell.py` sets up all of the nodes, both the master and worker nodes

- `send_ip_address.py` sends `ip_address.txt` to the master node with scp. `ip_address.txt` is where we store the IP addresses of our nodes. This will be helpful in spinning up our now configured nodes to do our work.


#### Step 6: Setup

Currently, our VMs need a little manual setup (this will be resolved and automated in the next iteration).

`$ cat tmp/ip_address.txt` to show you our IP addresses. For each IP address do the following:

1) `$ ssh -p 6174 rodrigocoelho@IP.ADDRESS.0.0`

2) `$ ./dotfiles/selenium_worker/manual_setup` - you will be asked to type sudo password. Type `swordfish` and press `Enter` for all prompts.

3) `$ exit` to leave remote VM

#### Step 7: Lastly, Activate our VMs to do work!

Now that our VMs are configured to scrape data, let's run `$ python3 activate.py`. 

If you ssh into our VMs and run `$ crontab -l`, you should see an output like this: `*/15 * * * * /home/rodrigocoelho/dotfiles/selenium_worker/collect.sh`

This tells us that crontabs is doing its job. Every 15 mins it will collect data and store it into the `selenium_worker/data` directory.

#### Step 8: Wait

Now our VMs are collecting data. After a few days (or weeks) you can run `$ python3 data_transfer.py` on your local computer to aggregate the data. This will send all the data collected from your remote VMs to your local computer via scp.

The next iteration will send this data to the master node periodically so you don't have to manually collect it.

#### Extra: What the data will look like

The data will come back as a json and look something like this:

```
{
    'f1-1520348192': {
        'description': 'd=2018-04-25;r=2018-04-30',
        'flight_id': 'f1',
        'price': $131,
        'city': 'nyc1',
        'unix': 1520348192
    }
}
```

#### Analyzing the Data

After we've run `python3 transfer_data.py` and checked that the data landed in our data directory, it's time to analyze the data:

`python3 analyze.py` will take each .txt file in our data directory, cleanse it in csv, and then move it into a pandas dataframe that in the end will be graphed.

Once you've executed analyze.py, check the `graphs` directory. There you should see a series of graphs.  

#### Features

- `$ python3 features/teardown.py` will teardown your droplets and delete the tmp/ip_address.txt as well as the json logs in the logs directory.

- `$ python3 features/activate.py` will update changes you make to the crontab for all VMs

- `$ python3 features/gitupdate.py` will make each VM git pull. This is great when you make changes to your code. 


#### How to manually ssh into a VM: 

ssh -p 6174 rodrigocoelho@IP.ADDRESS.0.0

IP.ADDRESS.0.0 will be found in tmp/ip_address.txt

#### NEXT STEPS

- AWS EC2 Instances for more locations  - Northern Virginia (DC), Ohio, Oregon 

- Use MongoDB to store data

- Collect data on more products/prices


#### Questions on Remote Server problems? 

Search: How to install and set up ________ on Ubuntu 16.04?
