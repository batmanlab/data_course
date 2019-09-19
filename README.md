# Exploratory Data Science Course (Early Access Build!)
*Brian Pollack (brianleepollack@gmail.com)*

This is the first iteration of the Exploratory Data Science Course for students in DBMI.  Because this is a highly interactive and computer-dependent class, many things will go wrong!  If there are any issues, especially with the setup and install, please contact me!

## Setup and Installation
*Note: If you already have Anaconda installed on the PSC, you can skip ahead to cloning the github repo.*

1. Login to PSC: `ssh -Y {your_username}@pghbio.bridges.psc.edu`
1. Check your projects and allocations:
    ```shell
    [userid@login018 ~]$ projects
     Your default charging project charge id is ABC0123456. If you would like to change the default charging project 
    use the command change_primary_group ~charge_id~. Use the charge id listed below for the project you would like 
    to make the default in place of ~charge_id~


    Project: XYZ654321D
    PI: My Principal Investigator
    Title: Important Research

        Resource: BRIDGES AI
      Allocation: 10,000.00
         Balance: 680.49
        End Date: 2030-07-15
    Award Active: Yes
     User Active: Yes
       Charge ID: ABC0123456
       *** Default charging project ***
     Directories:
         HOME /home/username

        Resource: BRIDGES LARGE MEMORY
      Allocation: 200,000.00
         Balance: 84,597.05
        End Date: 2030-07-15
    Award Active: Yes
     User Active: Yes
       Charge ID: ABC0123456
       *** Default charging project ***
     Directories:
         HOME /home/username

        Resource: BRIDGES PYLON STORAGE
      Allocation: 100,000.00
         Balance: 21,937.62
        End Date: 2030-07-15
    Award Active: Yes
     User Active: Yes
       Charge ID: ABC0123456
     Directories:
         Lustre Project Storage /pylon5/ABC0123456 
         Lustre Storage /pylon5/ABC0123456/username
    ```
1. Load into an interactive node: `interact -p {partition_name} --egress -t 02:00:00 -A {charge_id} --mem=120GB
	1. If you have access to charge ID 'bi561ip', use partition name 'DBMI'.
	1. If you don't, use partition name 'RM' or 'RM-small'
1. Navigate to your large-space directory: `cd $SCRATCH`
1. 
