# Local Private Server for RELEASE THE SPYCE secret fragrance

**Use at your own risk!**

---

### Requirements

- Python 3.7 or higher
- Android Device or Emulator (Modify your device's hosts file)
- [Modified Relefra apk](https://mega.nz/file/wYdkTRYJ#VUIetZRGFw6Jhiy5wk806TDktzzOO2FTtgpt8N8OAws)
- [Assets from img server](https://mega.nz/file/FRUQlI5b#yT4nrN9t6P-5mDsD3cJXRp0s3oOZSlFMrhn1lScUwrE)
- Self-Signed Certification (Run makecert.py / Install same cert on your device)
- install pip requirements by this command. 
```
pip install -r requirements.txt
```

---

### Not implemented features

- Base
  + Crafting weapons, items (recipe isn't available)
  + Spy expedition

- Shop & Exchange

- Achievement & Present

- Daily login bonus

- Battle result returns wrong rewards

- Stamina & Items will not consume
  + Stamina always setted max
  + Stamina valued 5000 but showing player level limit

- Spy Units
  + Fixed values at all (max lv, max ability board)
  + No weapon bonus skills
  
- AES-CBC-256 Encryption-Decryption networking (by original app)
  + sv-rtssf only works on modified app  
