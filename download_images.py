"""Downloads the official GTA Online artwork and vehicle pictures used by Kosatka Finance into assets/images/.
Run once on your own computer:   python download_images.py
Keep this script next to kosatka-finance-dashboard-login.html. The dashboard uses these local files first and
falls back to the online copy, then to its built-in illustrations, so missing files are never a problem."""
import os,urllib.request
HERE=os.path.dirname(os.path.abspath(__file__))
FILES={
"heists/fleeca.jpg": [
"https://www.gtabase.com/igallery/601-700/GTA_V_Artwork_Heists-629-1600.jpg"
],
"heists/prison.jpg": [
"https://www.gtabase.com/igallery/601-700/GTA_V_Artwork_Heists_2-630-1600.jpg"
],
"heists/humane.jpg": [
"https://www.gtabase.com/igallery/601-700/GTA_V_Artwork_Heists-629-1600.jpg"
],
"heists/seriesa.jpg": [
"https://www.gtabase.com/igallery/601-700/GTA_V_Artwork_Heists_2-630-1600.jpg"
],
"heists/pacific.jpg": [
"https://www.gtabase.com/igallery/601-700/GTA_V_Artwork_Heists_2-630-1600.jpg"
],
"heists/pacific-banner.jpg": [
"https://www.gtabase.com/igallery/601-700/GTA_V_Artwork_Heists-629-1600.jpg"
],
"heists/data-breaches.jpg": [
"https://www.gtabase.com/igallery/601-700/GTA_V_Artwork_DoomsdayHeist-647-1600.jpg"
],
"heists/bogdan.jpg": [
"https://www.gtabase.com/igallery/601-700/GTA_V_Artwork_DoomsdayHeist_2-648-1600.jpg"
],
"heists/doomsday.jpg": [
"https://www.gtabase.com/igallery/1501-1600/GTA_V_Artwork_DoomsdayHeist_3-1564-1600.jpg"
],
"heists/casino.jpg": [
"https://www.gtabase.com/igallery/4301-4400/GTA_V_Artwork_Diamond_Casino_Heist-4378-1600.jpg"
],
"heists/casino-banner.jpg": [
"https://www.gtabase.com/igallery/4301-4400/GTA_V_Artwork_Diamond_Casino_Heist_2-4398-1600.jpg"
],
"heists/cayo.jpg": [
"https://www.gtabase.com/igallery/7201-7300/GTA_V_Artwork_The_Cayo_Perico_Heist_2-7225-1600.jpg"
],
"heists/cayo-banner.jpg": [
"https://www.gtabase.com/igallery/7101-7200/GTA_V_Artwork_The_Cayo_Perico_Heist-7153-1600.jpg"
],
"heists/kortz.jpg": [
"https://www.gtabase.com/igallery/gta-online-artworks/gta-online-kortzcenterheist-dlc-1600.jpg"
],
"heists/kortz-banner.jpg": [
"https://www.gtabase.com/igallery/gta-online-screens/gtaonline-thekortzcenterheist-3-1080.jpg"
],
"heists/cluckin.jpg": [
"https://www.gtabase.com/igallery/gta-online-artworks/gtaonline-thecluckinbellfarmraid-artwork-1600.jpg"
],
"heists/oscar.jpg": [
"https://www.gtabase.com/igallery/gta-online-artworks/gtaonline-artwork-oscarguzman-fliesagain-1600.jpg"
],
"heists/oscar-banner.jpg": [
"https://www.gtabase.com/igallery/gta-online-screens/gta-online-oscar-guzman-flies-again-1080.jpg"
],
"heists/dre.jpg": [
"https://www.gtabase.com/igallery/8401-8500/GTAOnline_TheContract_Artwork-8406-1600.jpg"
],
"heists/dre-banner.jpg": [
"https://www.gtabase.com/igallery/8401-8500/gtaonline-thecontract-artwork-2-8451-1600.jpg"
],
"heists/bank.jpg": [
"https://www.gtabase.com/igallery/7401-7500/GTAOnline_LosSantos_Tuners_Artwork-7458-1600.jpg"
],
"heists/data-contract.jpg": [
"https://www.gtabase.com/igallery/7401-7500/GTAOnline_LosSantosTuners_Artwork_2-7499-1600.jpg"
],
"heists/superdollar.jpg": [
"https://www.gtabase.com/igallery/7401-7500/GTAOnline_LosSantos_Tuners_Artwork-7458-1600.jpg"
],
"heists/prison-contract.jpg": [
"https://www.gtabase.com/igallery/7401-7500/GTAOnline_LosSantosTuners_Artwork_2-7499-1600.jpg"
],
"heists/agency-deal.jpg": [
"https://www.gtabase.com/igallery/7401-7500/GTAOnline_LosSantos_Tuners_Artwork-7458-1600.jpg"
],
"heists/ecu.jpg": [
"https://www.gtabase.com/igallery/7401-7500/GTAOnline_LosSantosTuners_Artwork_2-7499-1600.jpg"
],
"heists/lost.jpg": [
"https://www.gtabase.com/igallery/7401-7500/GTAOnline_LosSantos_Tuners_Artwork-7458-1600.jpg"
],
"heists/union.jpg": [
"https://www.gtabase.com/igallery/7401-7500/GTAOnline_LosSantosTuners_Artwork_2-7499-1600.jpg"
],
"heists/gangbanger.jpg": [
"https://www.gtabase.com/igallery/gta-online-artworks/gtaonline-the-chop-shop-dlc-artwork-1600.jpg"
],
"heists/cargo-ship.jpg": [
"https://www.gtabase.com/igallery/gta-online-artworks/gta-online-the-chop-shop-2-1600.jpg"
],
"heists/duggan.jpg": [
"https://www.gtabase.com/igallery/gta-online-artworks/gtaonline-the-chop-shop-dlc-artwork-1600.jpg"
],
"heists/podium.jpg": [
"https://www.gtabase.com/igallery/gta-online-artworks/gta-online-the-chop-shop-2-1600.jpg"
],
"heists/mctony.jpg": [
"https://www.gtabase.com/igallery/gta-online-artworks/gtaonline-the-chop-shop-dlc-artwork-1600.jpg"
],
"cars/lm.jpg": [
"https://www.gtabase.com/igallery/7401-7500/GTAOnline_LosSantos_Tuners_Artwork-7458-1600.jpg"
],
"cars/wcc.jpg": [
"https://www.gtabase.com/igallery/601-700/GTA_V_Artwork_Gunrunning-645-1600.jpg"
],
"cars/ssa.jpg": [
"https://www.gtabase.com/igallery/1501-1600/GTA_V_Artwork_SuperSportSeries-1563-1600.jpg"
],
"missions/lamars-missions.jpg": [
"https://www.gtabase.com/igallery/gta-online-screens/gtaonline-contacts-lamar-1080.jpg"
],
"missions/lamars-lowriders.jpg": [
"https://www.gtabase.com/igallery/601-700/GTA_V_Artwork_LowRiders-634-1600.jpg"
],
"missions/geralds-last-play.jpg": [
"https://www.gtabase.com/igallery/6801-6900/GTA_Online_Artwork_GeraldsLastPlay_6NewMissions-6804-1600.png"
],
"missions/simeons-premium-deluxe-repo-work.jpg": [
"https://www.gtabase.com/igallery/601-700/GTA_V_Artwork_ImportExport-642-1600.jpg"
],
"missions/lesters-missions.jpg": [
"https://www.gtabase.com/igallery/601-700/GTA_V_Artwork_GTAOnline_Lester-683-1600.jpg"
],
"missions/martin-madrazos-missions.jpg": [
"https://www.gtabase.com/igallery/601-700/GTA_V_Artwork_HighLife-624-1600.jpg"
],
"missions/special-vehicle-work.jpg": [
"https://www.gtabase.com/igallery/601-700/GTA_V_Artwork_Executives-636-1600.jpg"
],
"missions/mobile-operations.jpg": [
"https://www.gtabase.com/igallery/601-700/GTA_V_Artwork_Gunrunning-645-1600.jpg"
],
"missions/casino-story-missions.jpg": [
"https://www.gtabase.com/igallery/3901-4000/GTA_V_Artwork_Diamond_Casino_Resort-3987-1600.jpg"
],
"missions/a-superyacht-life.jpg": [
"https://www.gtabase.com/igallery/6901-7000/GTA_Online_Artwork_GalaxySuperYacht-6985-1600.png"
],
"missions/franklin-lamars-short-trips.jpg": [
"https://www.gtabase.com/igallery/8501-8600/gtaonline-artwork-thecontract-shorttrips-8566-1600.jpg"
],
"missions/the-first-dose.jpg": [
"https://www.gtabase.com/igallery/8801-8900/gtaonline-lossantosdrugwars-1-8833-1600.jpg"
],
"missions/the-last-dose.jpg": [
"https://www.gtabase.com/igallery/8901-9000/gtaonline-lossantosdrugwars-thelastdose-artwork-8940-1600.jpg"
],
"missions/oscar-guzman-flies-again.jpg": [
"https://www.gtabase.com/igallery/gta-online-artworks/gtaonline-artwork-oscarguzman-fliesagain-1600.jpg"
],
"missions/the-cluckin-bell-farm-raid.jpg": [
"https://www.gtabase.com/igallery/gta-online-artworks/gtaonline-thecluckinbellfarmraid-artwork-1600.jpg"
],
"cars/niobe.jpg": [
"https://www.gtabase.com/images/gta-5/vehicles/sports/main/resized/niobe_320x180.jpg",
"https://www.gtabase.com/images/gta-5/vehicles/super/main/resized/niobe_320x180.jpg",
"https://www.gtabase.com/images/gta-5/vehicles/muscle/main/resized/niobe_320x180.jpg"
],
"cars/euros-x32.jpg": [
"https://www.gtabase.com/images/gta-5/vehicles/coupes/main/resized/euros-x32_320x180.jpg",
"https://www.gtabase.com/images/gta-5/vehicles/sports/main/resized/euros-x32_320x180.jpg",
"https://www.gtabase.com/images/gta-5/vehicles/super/main/resized/euros-x32_320x180.jpg",
"https://www.gtabase.com/images/gta-5/vehicles/muscle/main/resized/euros-x32_320x180.jpg"
],
"cars/itali-gto-stinger-tt.jpg": [
"https://www.gtabase.com/images/gta-5/vehicles/sports/main/resized/itali-gto-stinger-tt_320x180.jpg",
"https://www.gtabase.com/images/gta-5/vehicles/super/main/resized/itali-gto-stinger-tt_320x180.jpg",
"https://www.gtabase.com/images/gta-5/vehicles/muscle/main/resized/itali-gto-stinger-tt_320x180.jpg"
],
"cars/banshee-gts.jpg": [
"https://www.gtabase.com/images/gta-5/vehicles/sports/main/resized/banshee-gts_320x180.jpg",
"https://www.gtabase.com/images/gta-5/vehicles/super/main/resized/banshee-gts_320x180.jpg",
"https://www.gtabase.com/images/gta-5/vehicles/muscle/main/resized/banshee-gts_320x180.jpg"
],
"cars/deveste-eight.jpg": [
"https://www.gtabase.com/images/gta-5/vehicles/super/main/resized/deveste-eight_320x180.jpg",
"https://www.gtabase.com/images/gta-5/vehicles/sports/main/resized/deveste-eight_320x180.jpg",
"https://www.gtabase.com/images/gta-5/vehicles/muscle/main/resized/deveste-eight_320x180.jpg"
],
"cars/entity-mt.jpg": [
"https://www.gtabase.com/images/gta-5/vehicles/super/main/resized/entity-mt_320x180.jpg",
"https://www.gtabase.com/images/gta-5/vehicles/sports/main/resized/entity-mt_320x180.jpg",
"https://www.gtabase.com/images/gta-5/vehicles/muscle/main/resized/entity-mt_320x180.jpg"
],
"cars/la-coureuse.jpg": [
"https://www.gtabase.com/images/gta-5/vehicles/sports/main/resized/la-coureuse_320x180.jpg",
"https://www.gtabase.com/images/gta-5/vehicles/super/main/resized/la-coureuse_320x180.jpg",
"https://www.gtabase.com/images/gta-5/vehicles/muscle/main/resized/la-coureuse_320x180.jpg"
],
"cars/envisage.jpg": [
"https://www.gtabase.com/images/gta-5/vehicles/sports/main/resized/envisage_320x180.jpg",
"https://www.gtabase.com/images/gta-5/vehicles/super/main/resized/envisage_320x180.jpg",
"https://www.gtabase.com/images/gta-5/vehicles/muscle/main/resized/envisage_320x180.jpg"
],
"cars/paragon-s.jpg": [
"https://www.gtabase.com/images/gta-5/vehicles/sports/main/resized/paragon-s_320x180.jpg",
"https://www.gtabase.com/images/gta-5/vehicles/super/main/resized/paragon-s_320x180.jpg",
"https://www.gtabase.com/images/gta-5/vehicles/muscle/main/resized/paragon-s_320x180.jpg"
],
"cars/pipistrello.jpg": [
"https://www.gtabase.com/images/gta-5/vehicles/super/main/resized/pipistrello_320x180.jpg",
"https://www.gtabase.com/images/gta-5/vehicles/sports/main/resized/pipistrello_320x180.jpg",
"https://www.gtabase.com/images/gta-5/vehicles/muscle/main/resized/pipistrello_320x180.jpg"
],
"cars/coquette-d1.jpg": [
"https://www.gtabase.com/images/gta-5/vehicles/sports-classic/main/resized/coquette-d1_320x180.jpg",
"https://www.gtabase.com/images/gta-5/vehicles/sports/main/resized/coquette-d1_320x180.jpg",
"https://www.gtabase.com/images/gta-5/vehicles/super/main/resized/coquette-d1_320x180.jpg",
"https://www.gtabase.com/images/gta-5/vehicles/muscle/main/resized/coquette-d1_320x180.jpg"
],
"cars/baller-st-d.jpg": [
"https://www.gtabase.com/images/gta-5/vehicles/suvs/main/resized/baller-st-d_320x180.jpg",
"https://www.gtabase.com/images/gta-5/vehicles/sports/main/resized/baller-st-d_320x180.jpg",
"https://www.gtabase.com/images/gta-5/vehicles/super/main/resized/baller-st-d_320x180.jpg",
"https://www.gtabase.com/images/gta-5/vehicles/muscle/main/resized/baller-st-d_320x180.jpg"
],
"cars/aleutian.jpg": [
"https://www.gtabase.com/images/gta-5/vehicles/suvs/main/resized/aleutian_320x180.jpg",
"https://www.gtabase.com/images/gta-5/vehicles/sports/main/resized/aleutian_320x180.jpg",
"https://www.gtabase.com/images/gta-5/vehicles/super/main/resized/aleutian_320x180.jpg",
"https://www.gtabase.com/images/gta-5/vehicles/muscle/main/resized/aleutian_320x180.jpg"
],
"cars/pariah.jpg": [
"https://www.gtabase.com/images/gta-5/vehicles/sports/main/resized/pariah_320x180.jpg",
"https://www.gtabase.com/images/gta-5/vehicles/super/main/resized/pariah_320x180.jpg",
"https://www.gtabase.com/images/gta-5/vehicles/muscle/main/resized/pariah_320x180.jpg"
],
"cars/itali-rsx.jpg": [
"https://www.gtabase.com/images/gta-5/vehicles/super/main/resized/itali-rsx_320x180.jpg",
"https://www.gtabase.com/images/gta-5/vehicles/sports/main/resized/itali-rsx_320x180.jpg",
"https://www.gtabase.com/images/gta-5/vehicles/muscle/main/resized/itali-rsx_320x180.jpg"
],
"cars/tampa-gt.jpg": [
"https://www.gtabase.com/images/gta-5/vehicles/muscle/main/resized/tampa-gt_320x180.jpg",
"https://www.gtabase.com/images/gta-5/vehicles/sports/main/resized/tampa-gt_320x180.jpg",
"https://www.gtabase.com/images/gta-5/vehicles/super/main/resized/tampa-gt_320x180.jpg"
],
"cars/firebolt-asp.jpg": [
"https://www.gtabase.com/images/gta-5/vehicles/off-road/main/resized/firebolt-asp_320x180.jpg",
"https://www.gtabase.com/images/gta-5/vehicles/sports/main/resized/firebolt-asp_320x180.jpg",
"https://www.gtabase.com/images/gta-5/vehicles/super/main/resized/firebolt-asp_320x180.jpg",
"https://www.gtabase.com/images/gta-5/vehicles/muscle/main/resized/firebolt-asp_320x180.jpg"
],
"cars/castigator.jpg": [
"https://www.gtabase.com/images/gta-5/vehicles/suvs/main/resized/castigator_320x180.jpg",
"https://www.gtabase.com/images/gta-5/vehicles/sports/main/resized/castigator_320x180.jpg",
"https://www.gtabase.com/images/gta-5/vehicles/super/main/resized/castigator_320x180.jpg",
"https://www.gtabase.com/images/gta-5/vehicles/muscle/main/resized/castigator_320x180.jpg"
],
"cars/yosemite-1500.jpg": [
"https://www.gtabase.com/images/gta-5/vehicles/off-road/main/resized/yosemite-1500_320x180.jpg",
"https://www.gtabase.com/images/gta-5/vehicles/sports/main/resized/yosemite-1500_320x180.jpg",
"https://www.gtabase.com/images/gta-5/vehicles/super/main/resized/yosemite-1500_320x180.jpg",
"https://www.gtabase.com/images/gta-5/vehicles/muscle/main/resized/yosemite-1500_320x180.jpg"
],
"cars/terminus.jpg": [
"https://www.gtabase.com/images/gta-5/vehicles/off-road/main/resized/terminus_320x180.jpg",
"https://www.gtabase.com/images/gta-5/vehicles/sports/main/resized/terminus_320x180.jpg",
"https://www.gtabase.com/images/gta-5/vehicles/super/main/resized/terminus_320x180.jpg",
"https://www.gtabase.com/images/gta-5/vehicles/muscle/main/resized/terminus_320x180.jpg"
],
"cars/impaler-sz.jpg": [
"https://www.gtabase.com/images/gta-5/vehicles/muscle/main/resized/impaler-sz_320x180.jpg",
"https://www.gtabase.com/images/gta-5/vehicles/sports/main/resized/impaler-sz_320x180.jpg",
"https://www.gtabase.com/images/gta-5/vehicles/super/main/resized/impaler-sz_320x180.jpg"
],
"cars/cavalcade-xl.jpg": [
"https://www.gtabase.com/images/gta-5/vehicles/suvs/main/resized/cavalcade-xl_320x180.jpg",
"https://www.gtabase.com/images/gta-5/vehicles/sports/main/resized/cavalcade-xl_320x180.jpg",
"https://www.gtabase.com/images/gta-5/vehicles/super/main/resized/cavalcade-xl_320x180.jpg",
"https://www.gtabase.com/images/gta-5/vehicles/muscle/main/resized/cavalcade-xl_320x180.jpg"
],
"cars/dorado.jpg": [
"https://www.gtabase.com/images/gta-5/vehicles/suvs/main/resized/dorado_320x180.jpg",
"https://www.gtabase.com/images/gta-5/vehicles/sports/main/resized/dorado_320x180.jpg",
"https://www.gtabase.com/images/gta-5/vehicles/super/main/resized/dorado_320x180.jpg",
"https://www.gtabase.com/images/gta-5/vehicles/muscle/main/resized/dorado_320x180.jpg"
],
"cars/walton-l35.jpg": [
"https://www.gtabase.com/images/gta-5/vehicles/off-road/main/resized/walton-l35_320x180.jpg",
"https://www.gtabase.com/images/gta-5/vehicles/sports/main/resized/walton-l35_320x180.jpg",
"https://www.gtabase.com/images/gta-5/vehicles/super/main/resized/walton-l35_320x180.jpg",
"https://www.gtabase.com/images/gta-5/vehicles/muscle/main/resized/walton-l35_320x180.jpg"
],
"cars/pizza-boy.jpg": [
"https://www.gtabase.com/images/gta-5/vehicles/motorcycles/main/resized/pizza-boy_320x180.jpg",
"https://www.gtabase.com/images/gta-5/vehicles/sports/main/resized/pizza-boy_320x180.jpg",
"https://www.gtabase.com/images/gta-5/vehicles/super/main/resized/pizza-boy_320x180.jpg",
"https://www.gtabase.com/images/gta-5/vehicles/muscle/main/resized/pizza-boy_320x180.jpg"
],
"cars/keitora.jpg": [
"https://www.gtabase.com/images/gta-5/vehicles/utility/main/resized/keitora_320x180.jpg",
"https://www.gtabase.com/images/gta-5/vehicles/sports/main/resized/keitora_320x180.jpg",
"https://www.gtabase.com/images/gta-5/vehicles/super/main/resized/keitora_320x180.jpg",
"https://www.gtabase.com/images/gta-5/vehicles/muscle/main/resized/keitora_320x180.jpg"
],
"cars/caracara.jpg": [
"https://www.gtabase.com/images/gta-5/vehicles/off-road/main/resized/caracara_320x180.jpg",
"https://www.gtabase.com/images/gta-5/vehicles/sports/main/resized/caracara_320x180.jpg",
"https://www.gtabase.com/images/gta-5/vehicles/super/main/resized/caracara_320x180.jpg",
"https://www.gtabase.com/images/gta-5/vehicles/muscle/main/resized/caracara_320x180.jpg"
],
"cars/dominator-fx-interceptor.jpg": [
"https://www.gtabase.com/images/gta-5/vehicles/emergency/main/resized/dominator-fx-interceptor_320x180.jpg",
"https://www.gtabase.com/images/gta-5/vehicles/sports/main/resized/dominator-fx-interceptor_320x180.jpg",
"https://www.gtabase.com/images/gta-5/vehicles/super/main/resized/dominator-fx-interceptor_320x180.jpg",
"https://www.gtabase.com/images/gta-5/vehicles/muscle/main/resized/dominator-fx-interceptor_320x180.jpg"
],
"cars/impaler-lx-cruiser.jpg": [
"https://www.gtabase.com/images/gta-5/vehicles/emergency/main/resized/impaler-lx-cruiser_320x180.jpg",
"https://www.gtabase.com/images/gta-5/vehicles/sports/main/resized/impaler-lx-cruiser_320x180.jpg",
"https://www.gtabase.com/images/gta-5/vehicles/super/main/resized/impaler-lx-cruiser_320x180.jpg",
"https://www.gtabase.com/images/gta-5/vehicles/muscle/main/resized/impaler-lx-cruiser_320x180.jpg"
],
"cars/gauntlet-interceptor.jpg": [
"https://www.gtabase.com/images/gta-5/vehicles/emergency/main/resized/gauntlet-interceptor_320x180.jpg",
"https://www.gtabase.com/images/gta-5/vehicles/sports/main/resized/gauntlet-interceptor_320x180.jpg",
"https://www.gtabase.com/images/gta-5/vehicles/super/main/resized/gauntlet-interceptor_320x180.jpg",
"https://www.gtabase.com/images/gta-5/vehicles/muscle/main/resized/gauntlet-interceptor_320x180.jpg"
],
"cars/coquette-d10-pursuit.jpg": [
"https://www.gtabase.com/images/gta-5/vehicles/emergency/main/resized/coquette-d10-pursuit_320x180.jpg",
"https://www.gtabase.com/images/gta-5/vehicles/sports/main/resized/coquette-d10-pursuit_320x180.jpg",
"https://www.gtabase.com/images/gta-5/vehicles/super/main/resized/coquette-d10-pursuit_320x180.jpg",
"https://www.gtabase.com/images/gta-5/vehicles/muscle/main/resized/coquette-d10-pursuit_320x180.jpg"
],
"cars/ignus-pursuit.jpg": [
"https://www.gtabase.com/images/gta-5/vehicles/emergency/main/resized/ignus-pursuit_320x180.jpg",
"https://www.gtabase.com/images/gta-5/vehicles/sports/main/resized/ignus-pursuit_320x180.jpg",
"https://www.gtabase.com/images/gta-5/vehicles/super/main/resized/ignus-pursuit_320x180.jpg",
"https://www.gtabase.com/images/gta-5/vehicles/muscle/main/resized/ignus-pursuit_320x180.jpg"
],
"cars/greenwood-cruiser.jpg": [
"https://www.gtabase.com/images/gta-5/vehicles/emergency/main/resized/greenwood-cruiser_320x180.jpg",
"https://www.gtabase.com/images/gta-5/vehicles/sports/main/resized/greenwood-cruiser_320x180.jpg",
"https://www.gtabase.com/images/gta-5/vehicles/super/main/resized/greenwood-cruiser_320x180.jpg",
"https://www.gtabase.com/images/gta-5/vehicles/muscle/main/resized/greenwood-cruiser_320x180.jpg"
],
"cars/dorado-cruiser.jpg": [
"https://www.gtabase.com/images/gta-5/vehicles/emergency/main/resized/dorado-cruiser_320x180.jpg",
"https://www.gtabase.com/images/gta-5/vehicles/sports/main/resized/dorado-cruiser_320x180.jpg",
"https://www.gtabase.com/images/gta-5/vehicles/super/main/resized/dorado-cruiser_320x180.jpg",
"https://www.gtabase.com/images/gta-5/vehicles/muscle/main/resized/dorado-cruiser_320x180.jpg"
],
"cars/impaler-sz-cruiser.jpg": [
"https://www.gtabase.com/images/gta-5/vehicles/emergency/main/resized/impaler-sz-cruiser_320x180.jpg",
"https://www.gtabase.com/images/gta-5/vehicles/sports/main/resized/impaler-sz-cruiser_320x180.jpg",
"https://www.gtabase.com/images/gta-5/vehicles/super/main/resized/impaler-sz-cruiser_320x180.jpg",
"https://www.gtabase.com/images/gta-5/vehicles/muscle/main/resized/impaler-sz-cruiser_320x180.jpg"
],
"cars/outreach-faction.jpg": [
"https://www.gtabase.com/images/gta-5/vehicles/emergency/main/resized/outreach-faction_320x180.jpg",
"https://www.gtabase.com/images/gta-5/vehicles/sports/main/resized/outreach-faction_320x180.jpg",
"https://www.gtabase.com/images/gta-5/vehicles/super/main/resized/outreach-faction_320x180.jpg",
"https://www.gtabase.com/images/gta-5/vehicles/muscle/main/resized/outreach-faction_320x180.jpg"
],
"cars/benson.jpg": [
"https://www.gtabase.com/images/gta-5/vehicles/commercial/main/resized/benson_320x180.jpg",
"https://www.gtabase.com/images/gta-5/vehicles/sports/main/resized/benson_320x180.jpg",
"https://www.gtabase.com/images/gta-5/vehicles/super/main/resized/benson_320x180.jpg",
"https://www.gtabase.com/images/gta-5/vehicles/muscle/main/resized/benson_320x180.jpg"
],
"cars/boxville.jpg": [
"https://www.gtabase.com/images/gta-5/vehicles/vans/main/resized/boxville_320x180.jpg",
"https://www.gtabase.com/images/gta-5/vehicles/sports/main/resized/boxville_320x180.jpg",
"https://www.gtabase.com/images/gta-5/vehicles/super/main/resized/boxville_320x180.jpg",
"https://www.gtabase.com/images/gta-5/vehicles/muscle/main/resized/boxville_320x180.jpg"
]
}
def get(u):
    r=urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0','Referer':'https://www.gtabase.com/'})
    return urllib.request.urlopen(r,timeout=30).read()
ok=miss=0
for rel,urls in FILES.items():
    dest=os.path.join(HERE,'assets','images',*rel.split('/'))
    os.makedirs(os.path.dirname(dest),exist_ok=True)
    if os.path.exists(dest):print('have',rel);continue
    for u in urls:
        try:
            d=get(u)
            if len(d)>2000:open(dest,'wb').write(d);print('ok  ',rel);ok+=1;break
        except Exception:pass
    else:print('MISS',rel);miss+=1
print('done:',ok,'saved,',miss,'not found (the dashboard shows built-in art for those)')