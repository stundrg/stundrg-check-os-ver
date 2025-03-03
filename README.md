# stundrg-check-os-ver
- Detects and outputs the os version.

```

                                         :.                           
                                        :=:                           
                                       :-==                           
              :                   .:=-:=+==                           
             .-           .-      .:==:-=+*=-:                        
             .+-          :=  .=-::-**=====*#**+=:.                   
             .*+     ::.  :=::=++**==*#===+#***%%**+:                 
             :*+:    :==++=***##*+==-:-====********+=.                
            ..=+=.:==**+*#%#%@%##*=::.::-==+******=-==.               
             .:+**+*#*==+**#%%%#*-:---=--====*%%%*=--===:             
               =#%*%#+*%#=+%%%##*==**+=*==++++*##*=-:::.::            
                :+##*+*%%%%%#%%%%%##%***+=+++*##**+=-::::..:.         
                 .:=#*==*%%%*#*#%##%%%#***+=***+**+==-::==--:         
                   :-=::+###*#==**#%#*#%##*+=+*****+**+:-=---:        
                       .-*#+*=+++*#**%%%##-:-=*%#*=-+**=*====.        
                       :=*===.=+**=*%%%%%%= .%@%%%*-+****+==-.        
                      .-====+==**#%%%%%%#+  .*%%##*==++%%**==:        
                       :-=**###%%%%*##*-     :+==****-.:+*=+=         
                    .::::=+*-=+*####%%%#=    -**+**%@:..=++=:         
                  .:=##**--*%%*==+*###%%%===-:*++*#%%*::+==-          
                  .:=#%#**#%%%%#+*#%%#%%%%@%#===++*%%#-====.          
                 .::=**#%%#*%%#%%**%%%#+==#%%*=+***%%*=+==:           
                .::=**#%%#*+%####*#%%%*---=++=+=+*#%#===::.           
                ::=**=+*+++%@%%#**#%#*+=--=*++*#%%%##+=:.-            
     ::::     :::-**+==***#*#*****##*==-==.+%**%%%%%*=::::            
     .=**=:  .-.:-+*++**+==+*=+*+*#%##*+-=:.*%*#%%%%#*=*=             
      .:**+::::-===**#*+*****:-#*****+===-=::*##%%%%#==#.             
        :+***#=***+****=**##%=:*#@@+. :-+++=.:*#***++==*              
         .=**+********+*#%%%%+:=*%%-   :--*+::-**-:---*=              
          .-**=+*****#%%%%%%%*:=*%*:   .:::*#+=*+---=*%:              
         ..-=*##==##**#%%%%%%#::*=     :.==:=*++**###%%+              
        ..=#####*###%%%%%####*+===:    =*%#*=*++*#%%%%#:              
       .:=*#%%%%+=+===*%#+++*#=:...     :#%###**+*#%%#*.              
      .:=***###-      :*##****#*=:        =*#%%###%%%#*:              
    ..:=+++**+.    .-+*##%=+***%%+:          -**%%%%##*-              
   .:=****++-     .=*%%%%%+*%%%%%*=.          ::+*######=.            
  .:*%%#**+:       :*%%##+*%%%%#%#*:           :==****+#%#-           
 ..-%%%%%+:   ..:...=%****%%#%%#*+-.          .-==++===*%%#*:         
 ..=%%%%%-..:=*===++==+*#%%%%*-.             .-=::=++***%%##*-        
 ::+=#*#+:::::.-**+=+*#%%%%#=                --::+%%%#######%+:       
.--:=-==:==::-=+*++*#%##**+:                .==*##********###+:       
...-:-: ::.:=-::-=**##*=.                   .=***+=====+*+***+-==:.   
    ..     -:    ::-++-.                     :====+**=+*##*+==++-::.  
                 ..:==:                    .--=+***#*=+-*###***-..... 
                  .:-==:                  ....:+##*#*+:.=**###*===-.: 
                     ..                   :.=+++**+==*:.:+++--=+====::
                                          :-+====:. :--..+=:       -=-
                                          :=-          :.=-         ::
                                           :            .=.           
 ...  .    ... .:....    ......                                       
.-:=-----:.::=:====--::::===-:::::::::-:.    

```
### Use

```python
Use hi.py
$ pip install stundrg-check-os-ver
$ python # use hi
>>> from stundrg_check_os_ver.hi import hi
>>> hi()
$ python # use random_pic
>>> from stundrg_check_os_ver.hi import random_pic
>>> ramdom_pic()
```

```python
# $ pip install stundrg-check-os-ver
$ pip install --upgrade stundrg-check-os-ver
$ python
>>> from stundrg_check_os_ver.osver import get_os_ver as os
>>> os()
```
### Development environment setting
```bash
# install PDM
# git clone ...
$ source .venv/bin/activate
# pdm install
# $ vi ...

# TEST
$ pdm install
$ pdm test
$ pip install .

$ git add<FILE_NAME>
$ git push
$ pdm publish

Username:__token__
password : Token
```
### Test
- https://docs.pytest.org/en/stable/
```bash
# $ pdm add -dG test pytest pytest-cov
$ pytest
$ pytest -s
$ pytest --cov
```

### Ref
- https://pdm-project.org/en/latest/
- https://packaging.python.org/en/latest/tutorials/packaging-projects/
- console_scripts
