from nltk.corpus import wordnet as wn

# List of the building materials supported
materials = ['stone', 'gold', 'golden', 'brick', 'lava', 'water', 'stair']

# List of the commands supported
supported_commands = ['move', 'turn', 'build', 'save', 'go', 'tilt', 'pen', 'undo']

# List of the directions for movement supported
directions = ['left', 'right', 'back', 'forward', 'up', 'down']


# Given a list of strings, this maps every synonym of
# a given string to the string itself
def get_word_synonyms_as_dict(commands):
	synonyms_dict = {}

	for word in commands:
		synonyms_dict[word] = word

	for comm in commands:
		for word in get_word_synonyms(comm):
			synonyms_dict[word] = comm
	return synonyms_dict


def get_word_synonyms(word):
	synonyms = []
	comm_synonyms = wn.synsets(word, pos=wn.VERB)
	for word in comm_synonyms:
		for lemma in word.lemmas():
			if not (lemma.name() in synonyms):
				synonyms.append(lemma.name())
	return synonyms


# Required Dictionaries
directions_dict = get_word_synonyms_as_dict(directions)

materials_dict = {
	"air":0,
	"stone":1,
	"grass":2,
	"dirt":3,
	"cobblestone":4,
	"oak wood plank":5,
	"oak sapling":6,
	"bedrock":7,
	"flowing water":8,
	"still water":9,
	"flowing lava":10,
	"still lava":11,
	"sand":12,
	"gravel":13,
	"gold ore":14,
	"iron ore":15,
	"coal ore":16,
	"oak wood":17,
	"oak leaves":18,
	"sponge":19,
	"glass":20,
	"lapis lazuli ore":21,
	"lapis lazuli block":22,
	"dispenser":23,
	"sandstone":24,
	"note block":25,
	"bed":355,
	"powered rail":27,
	"detector rail":28,
	"sticky piston":29,
	"cobweb":30,
	"dead shrub":31,
	"dead bush":32,
	"piston":33,
	"piston head":34,
	"white wool":35,
	"dandelion":37,
	"poppy":38,
	"brown mushroom":39,
	"red mushroom":40,
	"gold":41,
	"iron":42,
	"double stone slab":43,
	"stone slab":44,
	"bricks":45,
	"tnt":46,
	"bookshelf":47,
	"moss stone":48,
	"obsidian":49,
	"torch":50,
	"fire":51,
	"monster spawner":52,
	"oak wood stairs":53,
	"chest":54,
	"redstone wire":55,
	"diamond ore":56,
	"diamond block":57,
	"crafting table":58,
	"wheat crops":59,
	"farmland":60,
	"furnace":61,
	"burning furnace":62,
	"standing sign block":63,
	"oak door block":64,
	"ladder":65,
	"rail":66,
	"cobblestone stairs":67,
	"wall-mounted sign block":68,
	"lever":69,
	"stone pressure plate":70,
	"iron door block":71,
	"wooden pressure plate":72,
	"redstone ore":73,
	"glowing redstone ore":74,
	"redstone torch ":76,
	"stone button":77,
	"snow":78,
	"ice":79,
	"snow block":80,
	"cactus":81,
	"clay":337,
	"sugar canes":338,
	"jukebox":84,
	"oak fence":85,
	"pumpkin":86,
	"netherrack":87,
	"soul sand":88,
	"glowstone":89,
	"nether portal":90,
	"jack o'lantern":91,
	"cake block":92,
	"redstone repeater block ":94,
	"white stained glass":95,
	"wooden trapdoor":96,
	"stone monster egg":97,
	"stone bricks":98,
	"brown mushroom block":99,
	"red mushroom block":100,
	"iron bars":101,
	"glass pane":102,
	"melon block":103,
	"pumpkin stem":104,
	"melon stem":105,
	"vines":106,
	"oak fence gate":107,
	"brick stairs":108,
	"stone brick stairs":109,
	"mycelium":110,
	"lily pad":111,
	"nether brick":405,
	"nether brick fence":113,
	"nether brick stairs":114,
	"nether wart":372,
	"enchantment table":116,
	"brewing stand":379,
	"cauldron":380,
	"end portal":119,
	"end portal frame":120,
	"end stone":121,
	"dragon egg":122,
	"redstone lamp ":124,
	"double oak wood slab":125,
	"oak wood slab":126,
	"cocoa":127,
	"sandstone stairs":128,
	"emerald ore":129,
	"ender chest":130,
	"tripwire hook":131,
	"tripwire":132,
	"emerald block":133,
	"spruce wood stairs":134,
	"birch wood stairs":135,
	"jungle wood stairs":136,
	"command block":137,
	"beacon":138,
	"cobblestone wall":139,
	"flower pot":390,
	"carrots":141,
	"potatoes":142,
	"wooden button":143,
	"mob head":144,
	"anvil":145,
	"trapped chest":146,
	"weighted pressure plate ":148,
	"redstone comparator ":150,
	"daylight sensor":151,
	"redstone block":152,
	"nether quartz ore":153,
	"hopper":154,
	"quartz block":155,
	"quartz stairs":156,
	"activator rail":157,
	"dropper":158,
	"white hardened clay":159,
	"white stained glass pane":160,
	"acacia leaves":161,
	"acacia wood":162,
	"acacia wood stairs":163,
	"dark oak wood stairs":164,
	"slime block":165,
	"barrier":166,
	"iron trapdoor":167,
	"prismarine":168,
	"sea lantern":169,
	"hay bale":170,
	"white carpet":171,
	"hardened clay":172,
	"block of coal":173,
	"packed ice":174,
	"sunflower":175,
	"free-standing banner":176,
	"wall-mounted banner":177,
	"inverted daylight sensor":178,
	"red sandstone":179,
	"red sandstone stairs":180,
	"double red sandstone slab":181,
	"red sandstone slab":182,
	"spruce fence gate":183,
	"birch fence gate":184,
	"jungle fence gate":185,
	"dark oak fence gate":186,
	"acacia fence gate":187,
	"spruce fence":188,
	"birch fence":189,
	"jungle fence":190,
	"dark oak fence":191,
	"acacia fence":192,
	"spruce door block":193,
	"birch door block":194,
	"jungle door block":195,
	"acacia door block":196,
	"dark oak door block":197,
	"end rod":198,
	"chorus plant":199,
	"chorus flower":200,
	"purpur block":201,
	"purpur pillar":202,
	"purpur stairs":203,
	"purpur double slab":204,
	"purpur slab":205,
	"end stone bricks":206,
	"beetroot block":207,
	"grass path":208,
	"end gateway":209,
	"repeating command block":210,
	"chain command block":211,
	"frosted ice":212,
	"magma block":213,
	"nether wart block":214,
	"red nether brick":215,
	"bone block":216,
	"structure void":217,
	"observer":218,
	"white shulker box":219,
	"orange shulker box":220,
	"magenta shulker box":221,
	"light blue shulker box":222,
	"yellow shulker box":223,
	"lime shulker box":224,
	"pink shulker box":225,
	"gray shulker box":226,
	"light gray shulker box":227,
	"cyan shulker box":228,
	"purple shulker box":229,
	"blue shulker box":230,
	"brown shulker box":231,
	"green shulker box":232,
	"red shulker box":233,
	"black shulker box":234,
	"white glazed terracotta":235,
	"orange glazed terracotta":236,
	"magenta glazed terracotta":237,
	"light blue glazed terracotta":238,
	"yellow glazed terracotta":239,
	"lime glazed terracotta":240,
	"pink glazed terracotta":241,
	"gray glazed terracotta":242,
	"light gray glazed terracotta":243,
	"cyan glazed terracotta":244,
	"purple glazed terracotta":245,
	"blue glazed terracotta":246,
	"brown glazed terracotta":247,
	"green glazed terracotta":248,
	"red glazed terracotta":249,
	"black glazed terracotta":250,
	"white concrete":251,
	"white concrete powder":252,
	"structure block":255,
	"iron shovel":256,
	"iron pickaxe":257,
	"iron axe":258,
	"flint and steel":259,
	"apple":260,
	"bow":261,
	"arrow":262,
	"coal":263,
	"diamond":264,
	"iron ingot":265,
	"gold ingot":266,
	"iron sword":267,
	"wooden sword":268,
	"wooden shovel":269,
	"wooden pickaxe":270,
	"wooden axe":271,
	"stone sword":272,
	"stone shovel":273,
	"stone pickaxe":274,
	"stone axe":275,
	"diamond sword":276,
	"diamond shovel":277,
	"diamond pickaxe":278,
	"diamond axe":279,
	"stick":280,
	"bowl":281,
	"mushroom stew":282,
	"golden sword":283,
	"golden shovel":284,
	"golden pickaxe":285,
	"golden axe":286,
	"string":287,
	"feather":288,
	"gunpowder":289,
	"wooden hoe":290,
	"stone hoe":291,
	"iron hoe":292,
	"diamond hoe":293,
	"golden hoe":294,
	"wheat seeds":295,
	"wheat":296,
	"bread":297,
	"leather helmet":298,
	"leather tunic":299,
	"leather pants":300,
	"leather boots":301,
	"chainmail helmet":302,
	"chainmail chestplate":303,
	"chainmail leggings":304,
	"chainmail boots":305,
	"iron helmet":306,
	"iron chestplate":307,
	"iron leggings":308,
	"iron boots":309,
	"diamond helmet":310,
	"diamond chestplate":311,
	"diamond leggings":312,
	"diamond boots":313,
	"golden helmet":314,
	"golden chestplate":315,
	"golden leggings":316,
	"golden boots":317,
	"flint":318,
	"raw porkchop":319,
	"cooked porkchop":320,
	"painting":321,
	"golden apple":322,
	"sign":323,
	"oak door":324,
	"bucket":325,
	"water bucket":326,
	"lava bucket":327,
	"minecart":328,
	"saddle":329,
	"iron door":330,
	"redstone":331,
	"snowball":332,
	"oak boat":333,
	"leather":334,
	"milk bucket":335,
	"brick":336,
	"paper":339,
	"book":340,
	"slimeball":341,
	"minecart with chest":342,
	"minecart with furnace":343,
	"egg":344,
	"compass":345,
	"fishing rod":346,
	"clock":347,
	"glowstone dust":348,
	"raw fish":349,
	"cooked fish":350,
	"ink sack":351,
	"bone":352,
	"sugar":353,
	"cake":354,
	"redstone repeater":356,
	"cookie":357,
	"map":358,
	"shears":359,
	"melon":360,
	"pumpkin seeds":361,
	"melon seeds":362,
	"raw beef":363,
	"steak":364,
	"raw chicken":365,
	"cooked chicken":366,
	"rotten flesh":367,
	"ender pearl":368,
	"blaze rod":369,
	"ghast tear":370,
	"gold nugget":371,
	"potion":373,
	"glass bottle":374,
	"spider eye":375,
	"fermented spider eye":376,
	"blaze powder":377,
	"magma cream":378,
	"eye of ender":381,
	"glistering melon":382,
	"bottle o' enchanting":384,
	"fire charge":385,
	"book and quill":386,
	"written book":387,
	"emerald":388,
	"item frame":389,
	"carrot":391,
	"potato":392,
	"baked potato":393,
	"poisonous potato":394,
	"empty map":395,
	"golden carrot":396,
	"mob head ":397,
	"carrot on a stick":398,
	"nether star":399,
	"pumpkin pie":400,
	"firework rocket":401,
	"firework star":402,
	"enchanted book":403,
	"redstone comparator":404,
	"nether quartz":406,
	"minecart with tnt":407,
	"minecart with hopper":408,
	"prismarine shard":409,
	"prismarine crystals":410,
	"raw rabbit":411,
	"cooked rabbit":412,
	"rabbit stew":413,
	"rabbit's foot":414,
	"rabbit hide":415,
	"armor stand":416,
	"iron horse armor":417,
	"golden horse armor":418,
	"diamond horse armor":419,
	"lead":420,
	"name tag":421,
	"minecart with command block":422,
	"raw mutton":423,
	"cooked mutton":424,
	"banner":425,
	"end crystal":426,
	"spruce door":427,
	"birch door":428,
	"jungle door":429,
	"acacia door":430,
	"dark oak door":431,
	"chorus fruit":432,
	"popped chorus fruit":433,
	"beetroot":434,
	"beetroot seeds":435,
	"beetroot soup":436,
	"dragon's breath":437,
	"splash potion":438,
	"spectral arrow":439,
	"tipped arrow":440,
	"lingering potion":441,
	"shield":442,
	"elytra":443,
	"spruce boat":444,
	"birch boat":445,
	"jungle boat":446,
	"acacia boat":447,
	"dark oak boat":448,
	"totem of undying":449,
	"shulker shell":450,
	"iron nugget":452,
	"knowledge book":453,
	"13 disc":2256,
	"cat disc":2257,
	"blocks disc":2258,
	"chirp disc":2259,
	"far disc":2260,
	"mall disc":2261,
	"mellohi disc":2262,
	"stal disc":2263,
	"strad disc":2264,
	"ward disc":2265,
	"11 disc":2266,
	"wait disc":2267
}