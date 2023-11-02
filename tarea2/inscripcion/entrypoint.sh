#!/bin/bash
sleep 20
exec python3 api.py &
exec python3 consumer.py