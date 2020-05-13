# <ins>UAA Minecraft Modding Guide</ins>  

## 1. Required Mods to Participate  
* Download all of the following mod _\.jar_ files.  

i. [Forge - Download the latest version by pressing _Installer_](http://files.minecraftforge.net)  
* Open-source modding API and loader

ii. [The Midnight](https://www.curseforge.com/minecraft/mc-mods/the-midnight/files/2942601)  
* The Midnight is a mod being developed by Cryptic Mushroom that adds a brand new dimension to explore full of unique adventures and dangers\! It's a dimension of perpetual darkness; the only light comes from crystals and the various flora, fungi, and fauna of the dimension\. You may travel willingly to this dimension, though you may unwillingly be dragged by a rifter into this strange, hostile world\.  

iii. [Biomes o' Plenty](https://www.curseforge.com/minecraft/mc-mods/biomes-o-plenty/files/2887034)  
* Biomes O' Plenty is an expansive biome mod for Minecraft that adds a slew of new, unique biomes to the Overworld and Nether!  To go along with the new biomes, it adds new plants, flowers, trees, building blocks, and much more\!  

iv. [TerraForged](https://www.curseforge.com/minecraft/mc-mods/terraforged/files/2953095)  
* TerraForged is an ambitious new terrain generator mod for Minecraft \(Java Edition\) attempting to create more immersive,
inspiring worlds to explore and build in\. Featuring an overhaul of the vanilla generation system, custom terrain shapes,
simulated erosion, better rivers, custom decorations, tonnes of configuration options, and more\!  

v. [Morpheus](https://www.curseforge.com/minecraft/mc-mods/morpheus/files/2898972)  
* Morpheus is a server\-only mod that adds sleep voting to a forge based server\. When a player sleeps, all other players in the same dimension are notified so it is easier to coordinate\. Also, you can configure a ratio of players that are required to make it morning \(default 50%\) messages can be customised in the config and alerts can be turned off if needed\.  

After you are done downloading the required mods and don't want to install shaders then skip to [3\. Installation Guide Using MultiMC](#3-installation-guide-using-multimc)\. However, if you want to install shaders then continue to the next section: [2\. Required Mods for Shaders](#2-required-mods-for-shaders)\.  

## 2. Required Mods for Shaders  
i. [OptiFine](https://optifine.net/adloadx?f=preview_OptiFine_1.15.2_HD_U_G1_pre16.jar)  
* OptiFine is a Minecraft optimization mod\. It allows Minecraft to run faster and look better with full support for HD textures and many configuration options\. The official OptiFine description is on the Minecraft Forums\.  

ii. [OptiForge](https://www.curseforge.com/minecraft/mc-mods/optiforge/files/2947809)  
* This mod can make OptiFine to be compatible with Forge\. This is an alternative before OptiFine has been officially compatible with Forge\. Although OptiFine 1\.15\.2 has been compatible with forge since G1 pre14, OptiForge will be compatible new forge version more fast, and there are an issue between OptiFine and other core mods which OptiForge fixed: [https://github.com/cpw/modlauncher/issues/37](https://github.com/cpw/modlauncher/issues/37)  

iii. [MixinBootstrap](https://www.curseforge.com/minecraft/mc-mods/mixinbootstrap/files/2939224)  
* MixinBootstrap is a temporary way of booting Mixin in a MinecraftForge production environment\. [https://github.com/LXGaming/MixinBootstrap](https://github.com/LXGaming/MixinBootstrap)  

iv. \(Optional\): You can use whatever shader you want as long as it's an [OptiFine](https://optifine.net/adloadx?f=preview_OptiFine_1.15.2_HD_U_G1_pre16.jar) compatible shader\. This is the shader I use and a few others on the server: [Sildur's Vibrant shaders v1\.27](https://sildurs-shaders.github.io/downloads)\. I personally use the Lite version and tweak the settings to my liking\.  
_Note: As found by Chung, after installing this shader mobs no longer flash red when hit\._

## 3. Installation Guide Using MultiMC  
* I highly recommend using MultiMC as it makes managing your Minecraft client much easier. However, if you still want to use the original launcher then use this part of the guide:  
[4\. Installation Guide Using Original Mojang Minecraft Laucher](#4-installation-guide-using-original-mojang-minecraft-laucher)  

i. [Download MultiMC](https://multimc.org/#Download)  

ii. Open up MultiMC and click profiles on the top right\.  
![000multimc.PNG](/screenshots/multimc/000multimc.PNG)  

iii. Click manage accounts  
![00multimc.PNG](/screenshots/multimc/00multimc.PNG)  

iv. Click _Add_ on the right and then enter in your Minecraft account information\.  
![0multimc.PNG](/screenshots/multimc/0multimc.PNG)  

v. Click _Add Instance_\.  
![1multimc.PNG](/screenshots/multimc/1multimc.PNG)  

vi. Name your instance, what group it falls under \(optional\) and choose Minecraft Vanilla version 1\.15\.2 and press _OK_\.  
![2multimc.PNG](/screenshots/multimc/2multimc.PNG)  

vii. Now right click your newly made instance and press _Edit Instance_\.  
![3multimc.PNG](/screenshots/multimc/3multimc.PNG)  

viii. Make sure _Version_ is selected on the left side column, then click _Install Forge_ on the right side column\.  
![4multimc.PNG](/screenshots/multimc/4multimc.PNG)  

ix. Select the latest version (highest number) which is 31\.1\.87 in my case, then click _OK_\.  
_Note: This might not be your case, but selecting the latest version should be sufficient_\.  
![5multimc.PNG](/screenshots/multimc/5multimc.PNG)  

x. Now you should see Forge. Now _Close_ the window\.  
![6multimc.PNG](/screenshots/multimc/6multimc.PNG)  

xi. Go ahead and start your instance by double\-clicking the instance that you created\. If it is installed correctly then you should see the Forge version you installed on the bottom left of the Minecraft main screen\. Also if you click _Mods_ you should see Forge there too\.  
![7multimc.PNG](/screenshots/multimc/7multimc.PNG)  
![8multimc.PNG](/screenshots/multimc/8multimc.PNG)  

xii. Now close your Minecraft game and right click your instance and press _Minecraft Folder_\. It will open up your the respective folder to your instance\.  
![9multimc.PNG](/screenshots/multimc/9multimc.PNG)  

xiii. Open up the _mods_ folder\.  
![10multimc.PNG](/screenshots/multimc/10multimc.PNG)  

xiv. Drag and drop the mod _\.jar_ files in the _mods_ folder\.  
![11multimc.PNG](/screenshots/multimc/11multimc.PNG)  
![12multimc.PNG](/screenshots/multimc/12multimc.PNG)  

xv. Now, once you open up your Minecraft game you should see all the mods that you installed\.  
![13multimc.PNG](/screenshots/multimc/13multimc.PNG)  
![14multimc.PNG](/screenshots/multimc/14multimc.PNG)  

## 4. Installation Guide Using Original Mojang Minecraft Laucher  

Just download MultiMC\. It will make your life so much easier\. I will even provide a link for you to go back to the top of the MultiMC section: [3\. Installation Guide Using MultiMC](#3-installation-guide-using-multimc)\.  
Maybe I'll write a guide here whenever I'm not lazy\.  
