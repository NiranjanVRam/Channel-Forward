# Running a Python Script
This repository contains a Python script that performs forwarding of all existing messages from multiple telegram channels to a single channel.

## Prerequisites
Before running the script, make sure you have the following installed:

- Python 3.12.2 (recommended)
- See requirements.txt for more dependencies.
- See [Configuration](#configuration) section for next steps.

## Getting Started
1. Clone this repository:

	```shell
	git clone https://github.com/NiranjanVRam/Channel-Forward.git
	```

2. Navigate to the project directory:

	```shell
	cd Channel-Forward
	```

3. Install the required dependencies:

	```shell
	pip install -U -r requirements.txt
	```

4. Run the script:

	```shell
	python forward.py
	```

## Configuration
- Replace the variables with your API ID, API Hash and phone number. Get these from [here](https://my.telegram.org/auth).
- Replace your channels variables with your channels' ids.
- Make sure to add -100 in front of your channel ids.

## Usage
After you have configured the script with appropriate parameters as mentioned above, see the [Get Started](#getting-started) section above.

## Contribution
- Contact the [developer](mailto:niranjanvram@gmail.com) for help on contributing.

## License
                    GNU GENERAL PUBLIC LICENSE
                       Version 3, 29 June 2007

 Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.