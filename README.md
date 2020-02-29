# CRASHED DDOS EXPLOIT

* Author: DMPRANKS200

This tool allows you to send forged UDP packets to Memcached servers obtained from Shodan.io

### Prerequisites

The only thing you need installed is Python 3.x

```
apt-get install python3
```

You also require to have Scapy and Shodan modules installed
```
pip install scapy
```

```
pip install shodan
```

### Using Shodan API

This tool requires you to own an upgraded Shodan API

You may obtain one for free in [Shodan](https://shodan.io/) if you sign up using a .edu email



### Using Docker

##### [Demo](**************)

You may deploy this tool to the cloud using a light Alpine Docker image.

> Note: Make sure to explicitly enter 'y' or 'n' to the interactive prompt

```bash
git clone https://
cd Crashed-DDoS-Exploit
echo "SHODAN_KEY" > api.txt
docker build -t memcrashed .
docker run -it memcrashed

```

