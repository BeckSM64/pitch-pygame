#!/bin/bash
# Launches the specified number of windows to allow for faster testing

# Get the argument as number of windows to launch
numPlayers=$1

# Get second argument to determine if server should be started
startServer=$2

# Check that an argument was provided
if [ -z "$numPlayers" ]
then
    echo "Error: Incorrect number of arguments. Provide number of players"
    exit 1
fi

# Ensure that the argument is an integer
regex='^[0-9]+$'
if ! [[ $numPlayers =~ $regex ]]
then
    echo "Error: Argument must be an integer"
    exit 1
fi

# Launch specified number of client windows
for i in $(seq 1 $numPlayers)
do
    python3 Pitch.py &
done

if [[ "$startServer" != "noserver" ]]
then
    # Launch server
    cd network
    python3 Server.py
fi
