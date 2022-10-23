# Local Private Server for RELEASE THE SPYCE secret fragrance

**Use at your own risk!**

**Resource files are not provided.**

---

### Requirements

- Python 3.7 or higher
- Android Device or Emulator (Needs modify hosts file)
- [Modified Relefra apk](https://mega.nz/file/AJ0DXaqA#hOiFlmsWZXwgFJBbrcLj2hvbV5ie-wGgv_pJKxaAoLc)
- Self-Signed Certification (run makecert.py / install same cert on your device)
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
  + It just shows empty list

- Daily login bonus
  + Needs modify api/mypage.py

- Battle result
  + It returns wrong rewards
  + recipe isn't available

- Stamina & Items will not consume
  + Stamina always setted max
  + Stamina valued 5000 but showing player level limit

- Spy Units
  + Fixed values at all (max lv, max board)
  + No weapon bonus skills
  
- AES-CBC-256 Encryption-Decryption networking (by original app)
  + sv-rtssf only works on modified app  
