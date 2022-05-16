# <span style="color:Green;">**Train Calculator**</span>

## <span style="color:lime;">*Description*</span>

The README is written in markdown and the program is written in python.

The program is made to calculate the time it takes for a train to travel a cross a line of stations, including stopping at each station.
It also compares the time with other trains or lines.

## <span style="color:lime;">*Languages*</span>

- Python
- Markdown

## <span style="color:lime;">*Requirements*</span>

- Python 3.10+
- Rich library

## <span style="color:lime;">*Installation*</span>

This project is made and tested for python 3.10 +. To install python visit (https://www.python.org/downloads) for the latest version.

Before running the program you need to install the rich library you can do this by typing "pip install rich" in your cmd.
If you are having problems installing rich please refer to their [website](https://rich.readthedocs.io/en/stable/)

You also need to clone the repository do this by opening your cmd and pasting in "git clone https://github.com/ElliotEriksson/End-Project".

## <span style="color:lime;">*Example*</span>

Do you want to

(1) Create new lines  

(2) Create new trains

(3) Create new trains and lines

(4) Calculate / Compare

(5) Exit the program

4

Do you want to (1) Compare one or more trains across a single line or (2) Compare one train across multiple lines? 1

<span style="color:red">Loading. . .</span><span style="color:lime"> ---------------------------------------- </span> <span style="color:purple"> 100% </span> <span style="color:skyblue">0:00:00</span>

-----[THE TRAINS]-----

(1) ['Stockholm - Uppsala', 'Stockholm C', '30000', 'Märsta', '12000', 'Knivsta', '17000', 'Uppsala C']

(2) ['Gröna Linjen', 'Gullmarsplan', '1000', 'Skanstull', '800', 'Medborgarplatsen', '450', 'Slussen', '500', 'Gamla Stan', '1000', 'T-Centralen']

Pick a line: 1

How many trains do you want to compare (1 if you just want to calculate for a single train)? 2

<span style="color:red">Loading. . .</span><span style="color:lime"> ---------------------------------------- </span> <span style="color:purple"> 100% </span> <span style="color:skyblue">0:00:00</span>

-----[THE LINES]-----

(1) ['X2000', '0.8', '56', '1.2']

(2) ['X55', '0.9', '56', '1.4']

Train nr1: 1

<span style="color:red">Loading. . .</span><span style="color:lime"> ---------------------------------------- </span> <span style="color:purple"> 100% </span> <span style="color:skyblue">0:00:00</span>s

Stockholm - Uppsala

Stockholm C

594 seconds

Märsta

273 seconds

Knivsta

362 seconds

Uppsala C

It takes a total of 1229 seconds to travel across Stockholm - Uppsala with the X2000.
This does not include stoppage time at the stations.

<span style="color:red">Loading. . .</span><span style="color:lime"> ---------------------------------------- </span> <span style="color:purple"> 100% </span> <span style="color:skyblue">0:00:00</span>

-----[THE LINES]-----

(1) ['X2000', '0.8', '56', '1.2']

(2) ['X55', '0.9', '56', '1.4']

Train nr2: 2

<span style="color:red">Loading. . .</span><span style="color:lime"> ---------------------------------------- </span> <span style="color:purple"> 100% </span> <span style="color:skyblue">0:00:00</span>

Stockholm - Uppsala

Stockholm C

587 seconds

Märsta

265 seconds

Knivsta

355 seconds

Uppsala C

It takes a total of 1207 seconds to travel across Stockholm - Uppsala with the X55.
This does not include stoppage time at the stations.

<span style="color:red">Loading. . .</span><span style="color:lime"> ---------------------------------------- </span> <span style="color:purple"> 100% </span> <span style="color:skyblue">0:00:00</span>

<span style="color:lightgreen">X55 is the fastest and takes </span><span style="color:skyblue">1207</span> <span style="color:lightgreen">seconds.</span>

<span style="color:red">X2000 is the slowest and takes </span><span style="color:skyblue">1229 <span style="color:red">seconds.</span>

The fastest train (X55) is 22 seconds faster than the slowest train (X2000).

Do you want to restart the program (y/n)? n

Thank you for using the program.

## <span style="color:lime;">*Roadmap*</span>

- [ ] Other Languages
- [ ] GUI
- [ ] More Trains
- [ ] More Lines

## <span style="color:lime;">*Changelog*</span>

### <span style="color:skyblue">Version 0.1</span>

#### <span style="color:lightgreen;">Added / Changed</span>

- Added file saving + loading for both trains and lines.
- Added the Train class.
- Added the calculations for stop and acceleration distance.

### <span style="color:skyblue">Version 0.2</span>

#### <span style="color:lightgreen;">Added / Changed</span>

- Added the calculations for the time between stops.
- Added the comparison of different trains across one line.

#### <span style="color:skyblue">Version 1.0</span>

#### <span style="color:lightgreen;">Added / Changed</span>

- Added the printing out of the values.
- Added reruns for invalid choices.

### <span style="color:skyblue;">Version 2.0</span>

#### <span style="color:lightgreen;">Added / Changed</span>

- Added comparison of one train across different lines.
- Added a nicer looking print.

### <span style="color:skyblue">Version 2.1</span>

#### <span style="color:lightgreen;">Added / Changed</span>

- Bug Fixes.
- Added end_program function.

### <span style="color:skyblue">Version 2.2</span>

#### <span style="color:lightgreen;">Added / Changed</span>

- Bug Fixes.
- Added a nicer looking print.
- Added README.

#### <span style="color:red;">Removed</span>

- Removed end_program function.

### <span style="color:skyblue">Verion 2.3</span>

#### <span style="color:lightgreen;">Added / Changed</span>

- Bug Fixes.
- Added loading function.

#### <span style="color:red;">Removed</span>

- Removed get_stats.

### <span style="color:skyblue">Version 2.4</span>

#### <span style="color:lightgreen;">Added / Changed</span>

- Bug Fixes.
- Added while loops to rerun for invalid inputs.

### <span style="color:skyblue">Version 2.5</span>

#### <span style="color:lightgreen;">Added / Changed</span>

- Bug Fixes
- Added more information to the README.

## <span style="color:lime;">*Contribution*</span>

Because this project is assessed pull request wont be allowed. After the assessment has been made they will be allowed (June 2022).

For bigger changes I wish for a issue to be open to dicuss said changes.

## <span style="color:lime;">*License*</span>

[MIT](https://choosealicense.com/licenses/mit/)

## <span style="color:lime;">*Contact*</span>

Elliot Eriksson - @Okand#3437, elliot@serait.se

[Repository](https://github.com/ElliotEriksson/End-Project)
