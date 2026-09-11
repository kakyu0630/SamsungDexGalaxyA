# Galaxy A Dex

# このソフトは似類のソフトがあることに加え、開発者がPixel7aに乗り換えA25を売却したため、開発終了します。
# ご利用ありがとうございました。

[  日本語 (Japanese) ](#-日本語-japanese) | [  English ](#-english)

---

## 🇯🇵 日本語 (Japanese)

Galaxy A Dex は、本来 Samsung DeX に非対応な Galaxy Aシリーズ（A20/A30/A25 等）で、PC上に仮想DeX画面を表示・操作するためのGUIアプリケーションです。

* **多言語自動切替:** OSの言語設定に合わせて自動で「日本語 / English」が切り替わります（UI上のドロップダウンメニューから手動切り替えも可能）。
* **クロスプラットフォーム対応:** リリース版は Windows 向け（単一exe）ですが、Pythonソースコードから実行することで macOS や Linux でも利用可能です。

---

### 📖 使い方

#### 事前準備
1. **PC側の準備（必須）:**
   起動時にエラーが発生する場合、Microsoft公式の **Visual C++ 再頒布可能パッケージ (x64)** が未インストールの可能性があります。あらかじめ以下のリンクからインストールしてください。
   * 🔗 [Visual C++ 再頒布可能パッケージ (x64) をダウンロード](https://aka.ms/vs/17/release/vc_redist.x64.exe)
2. **スマホ側の準備:**
   端末の「設定」>「端末情報」>「ソフトウェア情報」から「ビルド番号」を7回タップして**開発者モード**を有効化します。
3. 開発者向けオプションから **USBデバッグ**（または **ワイヤレスデバッグ**）を有効にしてください。

---

#### 1. USBで接続する場合

1. 本アプリを起動し、PCとスマホを USB Type-C ケーブルで接続します。
2. スマホ画面に「USBデバッグを許可しますか？」というポップアップが表示されたら**許可**をタップします。
3. アプリ上の「接続デバイス」一覧に端末名が表示されれば準備完了です。
   * ※表示されない場合はケーブルの抜き差しや「更新」ボタンをお試しください。

---

#### 2. ワイヤレスデバッグで接続する場合

1. スマホの「ワイヤレスデバッグ」項目を開き、「ペアリングコードでデバイスをペアリング」を選択します。
2. アプリの「ワイヤレス ADB 接続」エリアに、表示された **IP:ポート** と **ペアリングコード** を入力し、**「ペアリング」** ボタンをクリックします。
3. ペアリング成功後、次回以降の接続は「IP:ポート (接続用 :5555)」側にアドレスを入力し、**「接続」** ボタンを押すだけで完了します。

<div align="center">
  <img width="520" alt="Galaxy A Dex Main UI" src="https://github.com/user-attachments/assets/cb911be5-ec46-4d9a-80dc-f3eb56db6efd" />
</div>

---

#### 3. DeX 仮想ディスプレイの起動

1. **解像度・DPIの調整**（任意）
   * **幅 / 高さ:** お使いのPCモニターの解像度に合わせて変更できます（デフォルト: 1920x1080）。
   * **DPI:** 画面の要素が大きいと感じたら値を小さく、小さすぎると感じたら大きく調整してください（デフォルト: 240DPI）。
2. **「DeX 開始」** ボタンをクリックすると scrcpy がバックグラウンドで起動し、PC上に DeX 画面が表示されます。
3. **便利な操作:**
   * **F11 キー:** 全画面表示（フルスクリーン）の切り替え
   * **右 Alt キー** または **右 Ctrl キー:** マウスキャプチャの解除（PC側にカーソルを戻す）
4. **終了方法:** scrcpy のウィンドウを閉じるか、アプリ上の **「DeX 停止」** ボタンを押すことで安全に切断できます。

---

### ❓ トラブルシューティング

* **起動時にエラー（Line 6 や DLL 関連のエラーなど）が出て起動できない:**
  [Visual C++ 再頒布可能パッケージ (x64)](https://aka.ms/vs/17/release/vc_redist.x64.exe) をPCにインストールしてから再度起動してください。

---

### ⚠️ 注意事項

- **免責事項:** 本ソフトを利用したことによって生じた一切の損害や不利益について、作者は責任を負いません。自己責任でのご利用をお願いいたします。
- ワイヤレスデバッグ接続はネットワーク環境に依存するため、動作や安定性を保証するものではありません。
- 通常の S シリーズや Z シリーズでも利用可能ですが、動作保証対象外となります。

---

### 📱 動作確認済みデバイス

- **Galaxy A25 5G** (`SM-A253Z`, JP版 / 日本国内モデル)

---

### 🔗 リンク・コミュニティ

- [公式 Discord サーバー](https://discord.gg/gVqgBkvPRt)  
- [作者 X (旧Twitter)](https://x.com/kakyu0630)

---

## 🇺🇸 English

Galaxy A Dex is a GUI application designed to launch and operate a virtual Samsung DeX display on PCs for Galaxy A-series devices (such as A20, A30, A25, etc.) that do not natively support DeX.

* **Automatic Language Switching:** Automatically switches between Japanese and English based on system settings (manual switching via UI dropdown is also available).
* **Cross-Platform Support:** Official release is for Windows (standalone `.exe`), but running directly from Python source code allows execution on macOS and Linux.

---

### 📖 How to Use

#### Prerequisites
1. **PC Environment (Required):**
   If you encounter startup errors, the **Microsoft Visual C++ Redistributable (x64)** might be missing. Please download and install it from the link below:
   * 🔗 [Download Visual C++ Redistributable (x64)](https://aka.ms/vs/17/release/vc_redist.x64.exe)
2. **Phone Setup:**
   Go to **Settings** > **About phone** > **Software information** and tap **Build number** 7 times to enable **Developer options**.
3. Enable **USB debugging** (or **Wireless debugging**) in Developer options.

---

#### 1. Connecting via USB

1. Launch the application and connect your phone to the PC using a USB Type-C cable.
2. Tap **Allow** when the "Allow USB debugging?" prompt appears on your phone screen.
3. Once your device appears in the "Connected Device" list within the app, setup is complete.
   * *If it doesn't appear, try reconnecting the cable or clicking the "Refresh" button.*

---

#### 2. Connecting via Wireless Debugging

1. Open **Wireless debugging** on your phone and select **Pair device with pairing code**.
2. Enter the displayed **IP:Port** and **Pairing Code** into the "Wireless ADB Connection" section of the app, then click **Pair**.
3. After pairing successfully, for subsequent connections, simply enter the IP:Port in the lower connection input box (`:5555`) and click **Connect**.

<div align="center">
  <img width="520" alt="Galaxy A Dex Main UI" src="https://github.com/user-attachments/assets/cb911be5-ec46-4d9a-80dc-f3eb56db6efd" />
</div>

---

#### 3. Launching Samsung DeX

1. **Adjust Resolution & DPI** (Optional):
   * **Width / Height:** Match your PC monitor's resolution (Default: 1920x1080).
   * **DPI:** Lower the DPI if UI elements appear too large, or increase it if they appear too small (Default: 240 DPI).
2. Click **Start DeX**. `scrcpy` will launch in the background and display the DeX interface on your PC.
3. **Useful Controls:**
   * **F11:** Toggle Fullscreen Mode
   * **Right Alt** or **Right Ctrl:** Release mouse lock (return cursor to Windows/PC)
4. **How to Disconnect:** Close the `scrcpy` window or click **Stop DeX** in the application.

---

### ❓ Troubleshooting

* **App fails to start or shows errors (e.g., Line 6 or missing DLL errors):**
  Install the [Visual C++ Redistributable (x64)](https://aka.ms/vs/17/release/vc_redist.x64.exe) on your PC and launch the app again.

---

### ⚠️ Important Notes

- **Disclaimer:** The developer assumes no responsibility or liability for any issues, loss, or damages resulting from the use of this software.
- Wireless debugging functionality and stability depend on your network environment and are not guaranteed.
- While this application may function on flagship Galaxy S and Z series devices, operation on those models is not guaranteed.

---

### 📱 Confirmed Working Devices

- **Galaxy A25 5G** (`SM-A253Z`, JP version)

---

### 🔗 Links & Community

- [Official Discord](https://discord.gg/gVqgBkvPRt)  
- [Developer's Twitter / X](https://x.com/kakyu0630)
