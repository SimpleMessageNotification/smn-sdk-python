# smn-sdk-python


欢迎使用SMN服务Python SDK。SMN服务Python SDK 能简化你使用SMN服务的复杂程度。

Welcome to use the SMN Services Python SDK. SMN Services The Python SDK simplifies the complexity of your use of SMN services.


Install step:
1. Download sdk package in dist dir, that is  smn-sdk-python-1.0.0.zip
2. Unzip the package, then auto generate dir smn-sdk-python-1.0.0 in current dir.
3. cd into smn-sdk-python-1.0.0
4. exectue python setup.py install


Example for use sdk to send SMS：

You can open the smn-sdk-python-example/sendSmsDemo.py, config the domain_name/password, and the region_id which sign_id belong, sms sign_id, phoneNumber; then run the demo, it will send a sms message to the phoneNumber. The command is,

python sendSmsDemo.py
