# Backdoor
A backdoor is a programme that let you have control of a machine that gets affected by it basically giving you a backdoor acces to it

## How to install
You should have [python3](https://www.python.org/) installed on your pc, and 
You should also install all the required third party libraries 
<br/>
Installing a library 

    pip install library name
 
### Installing the backdoor 
First you have to download the project

    git clone https://github.com/rriiaad/Summer-challanges.git
    cd Summer-challanges/Personal Project

After that you will have to lanche the <strong> backdoor.py </strong> file on the computer you want to test it on after that lanche the <strong> server.py </strong> file and after you get a connexion you can start working 
<br/>
you can also compile the backdoor.py file to make an executable by using this commande
    
     pyinstaller .\backdoor.py --onefile --noconsole
     
if you don't have pyinstaller installed you should run this command

     pip install pyinstaller
     
## Fonctionalites
This backdoor can run on both Windows and linux and will grand you full controle of that computer, you can use all the systeme commandes you can execute programmes, you can take screenshots you umpload and download files and it's also persistent 
### Usage 
Before running this programe make sure to change the IP addres in both files to the ip addres of your serveur 
then you can run any systeme commande or any of these
#### Commands
| Command   | Description                                                                    |
| --------- | ------------------------------------------------------------------------------ |
| `screen`   | Takes a Screenshot of the victimes machine and downloading it                                                   |
| `upload`   | Upload file name, will let you send a file to the victimes machine                                                 |
| `download`   | download file name, will let you download any file from the victimes machine                                              |
| `exit`   | to close the connexion and stop the programe on both ends                                                   |

you can also execute any file just by writing down it's name

## Disclamer
- I'm not responsible of anything your are goging to do this with this
- Your are resposible for all your actions
- Your are not allowed to use this code without my permission and for now your not allowed :)
- This code was created for educational purposes only

