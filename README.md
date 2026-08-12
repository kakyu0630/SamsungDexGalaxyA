# Galaxy A Dex 日本語
Galaxy A Dexはその名の通りGalaxyのAシリーズ(A20やA30シリーズ)で、SamsungDexを起動するためのソフトです。  
リリース版はWindows版のみですがコードを改変すればmacOSやLinuxでも使用することが可能であると思われます。  

## 使い方
事前準備として開発者モードからUSBデバッグまたはワイヤレスデバッグを有効化してください。  
まずUSBで接続する方法から解説します。  
ソフトを起動したら端末側にデバッグ許可の画面が出てくるはずなので許可してください。これで完了です。  
仮に出てこなかったらType-Cの差し直し、手動更新などをお試しください。  
次にワイヤレスデバッグでの接続方法を解説します。  
ソフトを起動し、ワイヤレスデバッグのメニューを開き、専用コードでのペアリングを選択、表示されたIPアドレスとポート、ペアリングコードを入力し、ペアリングボタンをクリックします。  
成功したら接続完了という表記がソフト側に出てくるのでペアリングは完了です。  
ワイヤレスデバッグの場合次回接続時はワイヤレスデバッグメニューのIPアドレス、ポートをペアリング入力欄の一つ下の入力欄に入力し接続をしてください。  
これで接続は完了です。  
サンプルとしてソフトのメニューを置いておきます。  
<img width="621" height="692" alt="{DCBC1145-92DE-4F3B-91D0-A170FBEF7C2A}" src="https://github.com/user-attachments/assets/cb911be5-ec46-4d9a-80dc-f3eb56db6efd" />

次に実際にSamsungDexを起動するための方法を解説します。  
解像度やDPIを変更できますが、変更しなくても利用可能です。  
解像度はモニターの解像度に合わせ、DPIは実際に利用してみてでかいと思ったらDPIの値を低くし、大きいと思ったら値を大きくしてください。  
変更を済ませたらDex起動をクリックすれば、その後にScrcpyが起動し操作が可能になります。  
F11でフルスクリーン切り替えができますので是非ご活用ください。  
scrcpyを閉じるかソフト側でDex終了ボタンを押すことで切断することができます。  
### 注意事項
このソフトを利用したことで起こった不利益に関しては作者は責任を負いません。  
ワイヤレスデバッグでの接続は動作を保証しませんのでご注意ください。  
このソフトは通常のSやZシリーズでも利用することができますが、動作を保証しません。  

#### 動作を確認したデバイス
Galaxy A25 5G (SMA-253Z,JP)

##### リンク等について
[公式Discord](https://discord.gg/gVqgBkvPRt)  
[作者Twitter](https://x.com/kakyu0630)
# Galaxy A Dex　English


As the name suggests, Galaxy A Dex is a software application designed to enable and launch Samsung DeX on Galaxy A-series devices (such as the A20 or A30 series).  
While the official release is available only for Windows, it can likely be run on macOS or Linux by modifying the source code.

## How to Use

As a prerequisite, please enable **USB Debugging** or **Wireless Debugging** in your device's **Developer Options**.

### Connecting via USB

1. Launch the application.
2. Connect your device to your PC using a USB Type-C cable.
3. A prompt requesting debugging authorization should appear on your device screen. Grant permission to complete the setup.
4. If the authorization prompt does not appear, try reconnecting the USB Type-C cable or manually refreshing the connection in the app.

### Connecting via Wireless Debugging

1. Launch the application and open the **Wireless Debugging** menu.
2. Select **Pair with pairing code**.
3. Enter the displayed IP address, port, and pairing code, then click **Pair**.
4. Once successful, a completion message will appear in the app.
5. For subsequent connections, enter the IP address and port into the input fields located just below the pairing section and click connect.
<img width="522" height="692" alt="image" src="https://github.com/user-attachments/assets/051866ce-7292-47bd-aeac-b5d7cd299da3" />
---

### Launching Samsung DeX

1. Adjust the **Resolution** and **DPI** settings if necessary (default settings work fine as well):
   - **Resolution:** Match it to your monitor's display resolution.
   - **DPI:** Decrease the DPI value if elements appear too large, or increase it if they appear too small.
2. Click **Start DeX** (Dex起動).
3. **Scrcpy** will launch automatically, allowing you to control your device.
4. Press **F11** to toggle full-screen mode.
5. To disconnect, close the Scrcpy window or click **Stop DeX** (Dex終了) in the application.

---

## Important Notes

- **Disclaimer:** The developer assumes no responsibility or liability for any issues, loss, or damages resulting from the use of this software.
- Wireless debugging functionality and stability are not guaranteed.
- While this application may function on flagship Galaxy S and Z series devices, operation on those models is not guaranteed.

## Confirmed Working Devices

- **Galaxy A25 5G** (`SM-A253Z`, JP version)

## Links & Community

- [Official Discord](https://discord.gg/gVqgBkvPRt)
- [Developer's Twitter / X](https://x.com/kakyu0630)
