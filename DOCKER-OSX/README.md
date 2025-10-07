##### Código inicial para subir a maquina e gerar os numeros seriais unicos
```
docker run -it \
    --device /dev/kvm \
    -p 50022:10022 \
    -v /tmp/.X11-unix:/tmp/.X11-unix \
    -e "DISPLAY=${DISPLAY:-:0.0}" \
    -e GENERATE_UNIQUE=true \
    -e CPU='Haswell-noTSX' \
    -e CPUID_FLAGS='kvm=on,vendor=GenuineIntel,+invtsc,vmware-cpuid-freq=on' \
    -e GENERATE_UNIQUE=true \
    -e MASTER_PLIST_URL='https://raw.githubusercontent.com/sickcodes/osx-serial-generator/master/config-custom-sonoma.plist' \
    -e SHORTNAME=sequoia \
    sickcodes/docker-osx:latest
```

|DEVICE_MODEL |SERIAL      |BOARD_SERIAL     |
|:-----------:|:----------:|:---------------:|
|iMacPro1,1   |C02VXLY9HX87|C027533034NJG36JA|

|UUID                                |
|:----------------------------------:|
|67970125-34FE-4AEE-994D-71F80F3288F0|

|MAC_ADDRESS      |
|:---------------:|
|D0:3F:AA:6F:8D:97|

