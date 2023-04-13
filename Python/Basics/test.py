import multiprocessing
import telnetlib

def get_inventory(ip_address, username, password):
    # Telnet接続
    tn = telnetlib.Telnet(ip_address)

    # ユーザー名入力待ち
    tn.read_until(b"Username: ")
    tn.write(username.encode('ascii') + b"\n")

    # パスワード入力待ち
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

    # Cisco機器の場合
    if "cisco" in tn.read_until(b">").decode('ascii'):
        tn.write(b"enable\n")
        tn.read_until(b"Password: ")
        tn.write(b"enable_password\n")
        tn.read_until(b"#")
        tn.write(b"show inventory\n")
        inventory_output = tn.read_until(b"#").decode('ascii')
    # Juniper機器の場合
    elif "juniper" in tn.read_until(b">").decode('ascii'):
        tn.write(b"show chassis hardware\n")
        inventory_output = tn.read_until(b">").decode('ascii')
    else:
        raise ValueError("Unknown device type.")

    tn.write(b"exit\n")
    tn.read_all()

    return inventory_output

if __name__ == '__main__':
    # 例：CiscoとJuniper機器のIPアドレス、ユーザー名、パスワードをリストで定義
    devices = [
        {"ip_address": "192.168.126.132", "username": "cisco", "password": "cisco123"},
        {"ip_address": "192.168.126.133", "username": "cisco", "password": "cisco"},
        {"ip_address": "192.168.126.134", "username": "cisco", "password": "cisco"},


    ]


    with multiprocessing.Pool(processes=5) as pool:
        results = [pool.apply_async(get_inventory, (device['ip_address'], device['username'], device['password'])) for device in devices]

        for result, device in zip(results, devices):
            try:
                inventory_output = result.get(timeout=30)
                print(f"Inventory output for {device['ip_address']}:\n{inventory_output}")
            except Exception as e:
                print(f"Error connecting to {device['ip_address']}: {e}")
