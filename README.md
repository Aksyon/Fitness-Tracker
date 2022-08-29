# Fitness-Tracker

There is a fitness tracker module with three different sport activities:
Running, SportsWalking and Swimming.

It takes information from sensors, makes some calculations and give message with the next information:
type of activity, duration, distance, mean speed, spent calories.

Author: https://github.com/Aksyon / Aleksandr Aksyonov

How to start the program:

1) Import module Fitness-Tracker.

2) Create the package of information from sensors:
```python
packages = [('SWM', [720, 1, 80, 25, 40]),
            ('RUN', [15000, 1, 75]),
            ('WLK', [9000, 1, 75, 180])]
```
For swimming parameters are: step counts, duration (hours), weight, swimming pool length, how many times did you swim accros the pool;

for running: step counts, duration (hours), weight;

for sports walking: step counts, duration (hours), weight, heigth.

3) Call function read_package by using loop (for creating objects of classes Swimming/ SportsWalking/ Running).

4) Call function main for getting the message with different parameters of activity.

Example:
```python

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
```
Copyright [2022] [Aleksandr Aksyonov]
```
   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
   ```