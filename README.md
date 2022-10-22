# Local Private Server for RELEASE THE SPYCE secret fragrance

**Use at your own risk!**

**Resource files and certificate are not provided.**

---

### Requirements

- Python 3.7 or higher
- Your own Self-Signed Certification ( CN will be *.relefra.jp )
- Modified Relefra apk
- Android Device or Emulator (Needs modify hosts file)
- install pip requirements by this command. 
```
pip install -r requirements.txt
```

---

### Dosen't Working features

- Base
  + Crafting weapons, items
  + (recipe is not available)
  + Spy expedition
  + Always maximum friendly point (Lv10)

- Shop & Exchange

- Achievement & Present
  + It just shows empty list

- Gacha

- Daily login bonus
  + Needs modify api/mypage

- Battle result
  + It returns wrong rewards
  + recipe is not available

- Stamina & Items will not consume
  + Stamina setted max
  + Stamina valued 5000 but under player level limit
  + Items are moderately preloaded

- Spy Units
  + Fixed values at all (max lv, max board)
  + Edit data/_something_.json will allow edit values
  + Can't equip weapon (default weapon only)
  
- AES-CBC-256 Encryption-Decryption networking (original app)
  + This only works on modified app
