# ⚔️ Battle Quest: Clan Wars

A terminal-based RPG where players forge their destiny—fight solo in the arena or unite with clans to defeat the villain.

## 🎮 Gameplay Overview

### 🔐 Account Creation
- Enter a username and password (with confirmation)
- Auto-generated player profile with:
  - Random Item: Axe, Gun, Rocket Launcher, or Shovel
  - Random Stats:
    - Attack: 10-20
    - Defense: 15-25
    - Health: 300-500  
    - Agility: 30-60

### 🌟 Path Choices
1. Arena Path:  
   - Battle the **Wolf** (2000-3000 HP, 30-50 Attack) solo in turn-based combat.  
   - Winner gets glory; defeat means game over.

2. **Forest Path**:  
   - Join a **clan** (e.g., Shadow Hunters, Iron Defenders) for backup.  
   - Fight the **Villain** (stronger than Wolf) with clan allies.  
   - Win → Become clan leader; Lose → Honorary memorial.

## ⚡ **Battle Mechanics**
1. Agility check: Higher stat attacks first.
2. Damage formula: (Your Attack) - (Enemy Defense)  
3. Health deducts by net damage.
4. Repeat until one side's health ≤ 0.
