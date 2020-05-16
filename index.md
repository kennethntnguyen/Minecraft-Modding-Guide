# <ins>Minecraft Modding Guide</ins>  

## 1. Required Mods to Participate  
* Download all of the following mod _\.jar_ files.  

i. [The Midnight](https://www.curseforge.com/minecraft/mc-mods/the-midnight/files/2942601)  
* The Midnight is a mod being developed by Cryptic Mushroom that adds a brand new dimension to explore full of unique adventures and dangers\! It's a dimension of perpetual darkness; the only light comes from crystals and the various flora, fungi, and fauna of the dimension\. You may travel willingly to this dimension, though you may unwillingly be dragged by a rifter into this strange, hostile world\.  

ii. [Biomes o' Plenty](https://www.curseforge.com/minecraft/mc-mods/biomes-o-plenty/files/2887034)  
* Biomes O' Plenty is an expansive biome mod for Minecraft that adds a slew of new, unique biomes to the Overworld and Nether!  To go along with the new biomes, it adds new plants, flowers, trees, building blocks, and much more\!  

iii. [Morpheus](https://www.curseforge.com/minecraft/mc-mods/morpheus/files/2898972)  
* Morpheus is a server\-only mod that adds sleep voting to a forge based server\. When a player sleeps, all other players in the same dimension are notified so it is easier to coordinate\. Also, you can configure a ratio of players that are required to make it morning \(default 50%\) messages can be customised in the config and alerts can be turned off if needed\.  

After you are done downloading the required mods and don't want to install shaders or have shaders installed already then skip to [3\. Installing Mods Using MultiMC](#3-installing-mods-using-multimc)\. However, if you want to install shaders then continue to the next section: [2\. Required Mods for Shaders](#2-required-mods-for-shaders)\.  

## 2. Required Mods for Shaders  
i. [OptiFine](https://optifine.net/adloadx?f=preview_OptiFine_1.15.2_HD_U_G1_pre16.jar)  
* OptiFine is a Minecraft optimization mod\. It allows Minecraft to run faster and look better with full support for HD textures and many configuration options\. The official OptiFine description is on the Minecraft Forums\.  

ii. [OptiForge](https://www.curseforge.com/minecraft/mc-mods/optiforge/files/2947809)  
* This mod can make OptiFine to be compatible with Forge\. This is an alternative before OptiFine has been officially compatible with Forge\. Although OptiFine 1\.15\.2 has been compatible with forge since G1 pre14, OptiForge will be compatible new forge version more fast, and there are an issue between OptiFine and other core mods which OptiForge fixed: [https://github.com/cpw/modlauncher/issues/37](https://github.com/cpw/modlauncher/issues/37)  

iii. [MixinBootstrap](https://www.curseforge.com/minecraft/mc-mods/mixinbootstrap/files/2939224)  
* MixinBootstrap is a temporary way of booting Mixin in a MinecraftForge production environment\. [https://github.com/LXGaming/MixinBootstrap](https://github.com/LXGaming/MixinBootstrap)  

iv. [Sildur's Vibrant shaders v1\.27](https://sildurs-shaders.github.io/downloads) \(Optional\): You can use whatever shader you want as long as it's an [OptiFine](https://optifine.net/adloadx?f=preview_OptiFine_1.15.2_HD_U_G1_pre16.jar) compatible shader, works with Minecraft Version 1\.15\.2\. Sildur's Vibrant shaders v1\.27 is what I use and a few others on the server\. I personally use the Lite version and tweak the settings to my liking\.  
_Note: As found by Chung, after installing this shader mobs no longer flash red when hit\._

## 3. Installing Mods Using MultiMC  
* I highly recommend using MultiMC as it makes managing your Minecraft client much easier. However, if you still want to use the original launcher then use this part of the guide:  
[5\. Installing Mods Using Original Mojang Minecraft Laucher](#5-installing-mods-using-original-mojang-minecraft-laucher)\. If you already installed the _Required Mods_ and want to install the mods needed for shaders or already have Forge installed then skip to the [Install Shaders/Mods](#install-shaders) section\.  

i. [Download MultiMC](https://multimc.org/#Download)  

ii. Open up MultiMC and click profiles on the top right\.  
![a-multimc.png](/screenshots/multimc/a-multimc.png)  

iii. Click manage accounts  
![b-multimc.png](/screenshots/multimc/b-multimc.png)  

iv. Click _Add_ on the right and then enter in your Minecraft account information\.  
![c-multimc.png](/screenshots/multimc/c-multimc.png)  

v. Click _Add Instance_\.  
![d-multimc.png](/screenshots/multimc/d-multimc.png)  

vi. Name your instance, what group it falls under \(optional\) and choose Minecraft Vanilla version 1\.15\.2 and press _OK_\.  
![e-multimc.png](/screenshots/multimc/e-multimc.png)  

vii. Now right click your newly made instance and press _Edit Instance_\.  
![f-multimc.png](/screenshots/multimc/f-multimc.png)  

viii. Make sure _Version_ is selected on the left side column, then click _Install Forge_ on the right side column\.  
![g-multimc.png](/screenshots/multimc/g-multimc.png)  

ix. Select version _**31\.1\.93**_ in my case, then click _OK_\. Any later version will cause Minecraft to crash since Biomes O' Plenty hasn't updated yet.  
![h-multimc.png](/screenshots/multimc/h-multimc.png)  

x. Now you should see Forge. Now _Close_ the window\.  
![i-multimc.png](/screenshots/multimc/i-multimc.png)  

xi. Go ahead and start your instance by double\-clicking the instance that you created\. If it is installed correctly then you should see the Forge version you installed on the bottom left of the Minecraft main screen\. Also if you click _Mods_ you should see Forge there too\.  
_Note for people installing shaders: Make sure you do this step as it will create a directory for shaders\._  
![j-multimc.png](/screenshots/multimc/j-multimc.png)   
![k-multimc.png](/screenshots/multimc/k-multimc.png)  

<a name="install-shaders"></a><a name="install-mods"></a>
xii. Now close your Minecraft game and right click your instance and press _Minecraft Folder_\. It will open up your the respective folder to your instance\.  
![l-multimc.png](/screenshots/multimc/l-multimc.png)  

xiii. Open up the _mods_ folder\.  
![m-multimc.png](/screenshots/multimc/m-multimc.png)  

xiv. Drag and drop the mod _\.jar_ files in the _mods_ folder\. If you are installing shaders then make sure you put OptiFine, OptiForge and MixinBootloader _\.jar_ files here too\.  
![n-multimc.png](/screenshots/multimc/n-multimc.png)  
![o-multimc.png](/screenshots/multimc/o-multimc.png)  

xv. Now, once you open up your Minecraft game you should see all the mods that you installed\.  
![p-multimc.png](/screenshots/multimc/p-multimc.png)  
![q-multimc.png](/screenshots/multimc/q-multimc.png)  

xvi. If you installed OptiFine then you should see the version of OptiFine that you installed\.
![r-multimc.png](/screenshots/multimc/r-multimc.png)  
![s-multimc.png](/screenshots/multimc/s-multimc.png)  
![t-multimc.png](/screenshots/multimc/t-multimc.png)  
_Optional: Proceed to the [next section](#4-installing-shaders-using-multimc) for steps on how to install a shaderpack to your Minecraft instance\._

## 4. Installing Shaders Using MultiMC
i. This section is for those that installed mods from sections: [1\. Required Mods to Participate](#1-required-mods-to-participate) and [2\. Required Mods for Shaders](#2-required-mods-for-shaders). If you haven't then refer to those sections \(1 & 2\) and section [3\. Installing Mods Using MultiMC](#3-installing-mods-using-multimc) for a guide on installtion\.  

ii. Open MultiMC, right click your instance and click _Minecraft Folder_\.  
![a-multimc-shaders.png](/screenshots/multimc/shaders/a-multimc-shaders.png)  

iii. You will see a _shaderpacks_ folder\. Open this folder\.  
![b-multimc-shaders.png](/screenshots/multimc/shaders/b-multimc-shaders.png)  

iv. Drag & Drop your shader \.zip file into the _shaderpacks_ folder\.  
![c-multimc-shaders.png](/screenshots/multimc/shaders/c-multimc-shaders.png)  

v. Now you just need to enable those shaders in\-game\. Once you have your game open, click _Options\.\.\._, _Video Settings\.\.\._, _Shaders\.\.\._ and select by clicking the shader you just installed\.  
![d-multimc-shaders.png](/screenshots/multimc/shaders/d-multimc-shaders.png)  

vi. That's it. Your game should be ready to go with your newly installed shaders\.

## 5. Installing Mods Using Original Mojang Minecraft Laucher  

i. [Forge - Download the latest version by pressing _Installer_](http://files.minecraftforge.net)  
* Open-source modding API and loader

Just download MultiMC\. It will make your life so much easier\. I will even provide a link for you to go back to the top of the MultiMC section: [3\. Installing Mods Using MultiMC](#3-installing-mods-using-multimc)\.  
Maybe I'll write a guide here whenever I have nothing else to do\.  
