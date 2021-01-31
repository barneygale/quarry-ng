# !!! auto-generated - do not edit !!!
from quarry.native import *
edition = 'pc'
release = '1.7'
version = 5
packet_init_down = Container(fields=[{'name': 'name', 'type': Mapper(type=VarInt(bits=32), mappings={})}, {'name': 'params', 'type': Switch(fields={}, compareTo='name', default=None)}])
packet_init_up = Container(fields=[{'name': 'name', 'type': Mapper(type=VarInt(bits=32), mappings={'0x00': 'set_protocol', '0xfe': 'legacy_server_list_ping'})}, {'name': 'params', 'type': Switch(fields={'set_protocol': Container(fields=[{'name': 'protocolVersion', 'type': VarInt(bits=32)}, {'name': 'serverHost', 'type': String(countType=VarInt(bits=32))}, {'name': 'serverPort', 'type': Struct(fmt='>H')}, {'name': 'nextState', 'type': VarInt(bits=32)}]), 'legacy_server_list_ping': Container(fields=[{'name': 'payload', 'type': Struct(fmt='B')}])}, compareTo='name', default=None)}])
packet_status_down = Container(fields=[{'name': 'name', 'type': Mapper(type=VarInt(bits=32), mappings={'0x00': 'server_info', '0x01': 'ping'})}, {'name': 'params', 'type': Switch(fields={'server_info': Container(fields=[{'name': 'response', 'type': String(countType=VarInt(bits=32))}]), 'ping': Container(fields=[{'name': 'time', 'type': Struct(fmt='>q')}])}, compareTo='name', default=None)}])
packet_status_up = Container(fields=[{'name': 'name', 'type': Mapper(type=VarInt(bits=32), mappings={'0x00': 'ping_start', '0x01': 'ping'})}, {'name': 'params', 'type': Switch(fields={'ping_start': Container(fields=[]), 'ping': Container(fields=[{'name': 'time', 'type': Struct(fmt='>q')}])}, compareTo='name', default=None)}])
packet_login_down = Container(fields=[{'name': 'name', 'type': Mapper(type=VarInt(bits=32), mappings={'0x00': 'disconnect', '0x01': 'encryption_begin', '0x02': 'success'})}, {'name': 'params', 'type': Switch(fields={'disconnect': Container(fields=[{'name': 'reason', 'type': String(countType=VarInt(bits=32))}]), 'encryption_begin': Container(fields=[{'name': 'serverId', 'type': String(countType=VarInt(bits=32))}, {'name': 'publicKey', 'type': ByteArray(count=None, countType=Struct(fmt='>h'))}, {'name': 'verifyToken', 'type': ByteArray(count=None, countType=Struct(fmt='>h'))}]), 'success': Container(fields=[{'name': 'uuid', 'type': String(countType=VarInt(bits=32))}, {'name': 'username', 'type': String(countType=VarInt(bits=32))}])}, compareTo='name', default=None)}])
packet_login_up = Container(fields=[{'name': 'name', 'type': Mapper(type=VarInt(bits=32), mappings={'0x00': 'login_start', '0x01': 'encryption_begin'})}, {'name': 'params', 'type': Switch(fields={'login_start': Container(fields=[{'name': 'username', 'type': String(countType=VarInt(bits=32))}]), 'encryption_begin': Container(fields=[{'name': 'sharedSecret', 'type': ByteArray(count=None, countType=Struct(fmt='>h'))}, {'name': 'verifyToken', 'type': ByteArray(count=None, countType=Struct(fmt='>h'))}])}, compareTo='name', default=None)}])
packet_play_down = Container(fields=[{'name': 'name', 'type': Mapper(type=VarInt(bits=32), mappings={'0x00': 'keep_alive', '0x01': 'login', '0x02': 'chat', '0x03': 'update_time', '0x04': 'entity_equipment', '0x05': 'spawn_position', '0x06': 'update_health', '0x07': 'respawn', '0x08': 'position', '0x09': 'held_item_slot', '0x0a': 'bed', '0x0b': 'animation', '0x0c': 'named_entity_spawn', '0x0d': 'collect', '0x0e': 'spawn_entity', '0x0f': 'spawn_entity_living', '0x10': 'spawn_entity_painting', '0x11': 'spawn_entity_experience_orb', '0x12': 'entity_velocity', '0x13': 'entity_destroy', '0x14': 'entity', '0x15': 'rel_entity_move', '0x16': 'entity_look', '0x17': 'entity_move_look', '0x18': 'entity_teleport', '0x19': 'entity_head_rotation', '0x1a': 'entity_status', '0x1b': 'attach_entity', '0x1c': 'entity_metadata', '0x1d': 'entity_effect', '0x1e': 'remove_entity_effect', '0x1f': 'experience', '0x20': 'update_attributes', '0x21': 'map_chunk', '0x22': 'multi_block_change', '0x23': 'block_change', '0x24': 'block_action', '0x25': 'block_break_animation', '0x26': 'map_chunk_bulk', '0x27': 'explosion', '0x28': 'world_event', '0x29': 'named_sound_effect', '0x2a': 'world_particles', '0x2b': 'game_state_change', '0x2c': 'spawn_entity_weather', '0x2d': 'open_window', '0x2e': 'close_window', '0x2f': 'set_slot', '0x30': 'window_items', '0x31': 'craft_progress_bar', '0x32': 'transaction', '0x33': 'update_sign', '0x34': 'map', '0x35': 'tile_entity_data', '0x36': 'open_sign_entity', '0x37': 'statistics', '0x38': 'player_info', '0x39': 'abilities', '0x3a': 'tab_complete', '0x3b': 'scoreboard_objective', '0x3c': 'scoreboard_score', '0x3d': 'scoreboard_display_objective', '0x3e': 'scoreboard_team', '0x3f': 'custom_payload', '0x40': 'kick_disconnect'})}, {'name': 'params', 'type': Switch(fields={'keep_alive': Container(fields=[{'name': 'keepAliveId', 'type': Struct(fmt='>i')}]), 'login': Container(fields=[{'name': 'entityId', 'type': Struct(fmt='>i')}, {'name': 'gameMode', 'type': Struct(fmt='B')}, {'name': 'dimension', 'type': Struct(fmt='b')}, {'name': 'difficulty', 'type': Struct(fmt='B')}, {'name': 'maxPlayers', 'type': Struct(fmt='B')}, {'name': 'levelType', 'type': String(countType=VarInt(bits=32))}]), 'chat': Container(fields=[{'name': 'message', 'type': String(countType=VarInt(bits=32))}]), 'update_time': Container(fields=[{'name': 'age', 'type': Struct(fmt='>q')}, {'name': 'time', 'type': Struct(fmt='>q')}]), 'entity_equipment': Container(fields=[{'name': 'entityId', 'type': Struct(fmt='>i')}, {'name': 'slot', 'type': Struct(fmt='>h')}, {'name': 'item', 'type': Container(fields=[{'name': 'blockId', 'type': Struct(fmt='>h')}, {'anon': True, 'type': Switch(fields={'-1': Void()}, compareTo='blockId', default=Container(fields=[{'name': 'itemCount', 'type': Struct(fmt='b')}, {'name': 'itemDamage', 'type': Struct(fmt='>h')}, {'name': 'nbtData', 'type': NBT()}]))}])}]), 'spawn_position': Container(fields=[{'name': 'location', 'type': Container(fields=[{'name': 'x', 'type': Struct(fmt='>i')}, {'name': 'y', 'type': Struct(fmt='>i')}, {'name': 'z', 'type': Struct(fmt='>i')}])}]), 'update_health': Container(fields=[{'name': 'health', 'type': Struct(fmt='>f')}, {'name': 'food', 'type': Struct(fmt='>h')}, {'name': 'foodSaturation', 'type': Struct(fmt='>f')}]), 'respawn': Container(fields=[{'name': 'dimension', 'type': Struct(fmt='>i')}, {'name': 'difficulty', 'type': Struct(fmt='B')}, {'name': 'gamemode', 'type': Struct(fmt='B')}, {'name': 'levelType', 'type': String(countType=VarInt(bits=32))}]), 'position': Container(fields=[{'name': 'x', 'type': Struct(fmt='>d')}, {'name': 'y', 'type': Struct(fmt='>d')}, {'name': 'z', 'type': Struct(fmt='>d')}, {'name': 'yaw', 'type': Struct(fmt='>f')}, {'name': 'pitch', 'type': Struct(fmt='>f')}, {'name': 'onGround', 'type': Struct(fmt='?')}]), 'held_item_slot': Container(fields=[{'name': 'slot', 'type': Struct(fmt='b')}]), 'bed': Container(fields=[{'name': 'entityId', 'type': Struct(fmt='>i')}, {'name': 'location', 'type': Container(fields=[{'name': 'x', 'type': Struct(fmt='>i')}, {'name': 'y', 'type': Struct(fmt='B')}, {'name': 'z', 'type': Struct(fmt='>i')}])}]), 'animation': Container(fields=[{'name': 'entityId', 'type': VarInt(bits=32)}, {'name': 'animation', 'type': Struct(fmt='B')}]), 'named_entity_spawn': Container(fields=[{'name': 'entityId', 'type': VarInt(bits=32)}, {'name': 'playerUUID', 'type': String(countType=VarInt(bits=32))}, {'name': 'playerName', 'type': String(countType=VarInt(bits=32))}, {'name': 'data', 'type': Array(type=Container(fields=[{'name': 'name', 'type': String(countType=VarInt(bits=32))}, {'name': 'value', 'type': String(countType=VarInt(bits=32))}, {'name': 'signature', 'type': String(countType=VarInt(bits=32))}]), count=None, countType=VarInt(bits=32))}, {'name': 'x', 'type': Struct(fmt='>i')}, {'name': 'y', 'type': Struct(fmt='>i')}, {'name': 'z', 'type': Struct(fmt='>i')}, {'name': 'yaw', 'type': Struct(fmt='b')}, {'name': 'pitch', 'type': Struct(fmt='b')}, {'name': 'currentItem', 'type': Struct(fmt='>h')}, {'name': 'metadata', 'type': EntityMetadataArray(type=Switch(fields={'0': Struct(fmt='b'), '1': Struct(fmt='>h'), '2': Struct(fmt='>i'), '3': Struct(fmt='>f'), '4': String(countType=VarInt(bits=32)), '5': Container(fields=[{'name': 'blockId', 'type': Struct(fmt='>h')}, {'anon': True, 'type': Switch(fields={'-1': Void()}, compareTo='blockId', default=Container(fields=[{'name': 'itemCount', 'type': Struct(fmt='b')}, {'name': 'itemDamage', 'type': Struct(fmt='>h')}, {'name': 'nbtData', 'type': NBT()}]))}]), '6': Container(fields=[{'name': 'x', 'type': Struct(fmt='>i')}, {'name': 'y', 'type': Struct(fmt='>i')}, {'name': 'z', 'type': Struct(fmt='>i')}]), '7': Container(fields=[{'name': 'pitch', 'type': Struct(fmt='>f')}, {'name': 'yaw', 'type': Struct(fmt='>f')}, {'name': 'roll', 'type': Struct(fmt='>f')}])}, compareTo='type', default=None), endVal=127)}]), 'collect': Container(fields=[{'name': 'collectedEntityId', 'type': Struct(fmt='>i')}, {'name': 'collectorEntityId', 'type': Struct(fmt='>i')}]), 'spawn_entity': Container(fields=[{'name': 'entityId', 'type': VarInt(bits=32)}, {'name': 'type', 'type': Struct(fmt='b')}, {'name': 'x', 'type': Struct(fmt='>i')}, {'name': 'y', 'type': Struct(fmt='>i')}, {'name': 'z', 'type': Struct(fmt='>i')}, {'name': 'pitch', 'type': Struct(fmt='b')}, {'name': 'yaw', 'type': Struct(fmt='b')}, {'name': 'objectData', 'type': Container(fields=[{'name': 'intField', 'type': Struct(fmt='>i')}, {'name': 'velocityX', 'type': Switch(fields={'0': Void()}, compareTo='intField', default=Struct(fmt='>h'))}, {'name': 'velocityY', 'type': Switch(fields={'0': Void()}, compareTo='intField', default=Struct(fmt='>h'))}, {'name': 'velocityZ', 'type': Switch(fields={'0': Void()}, compareTo='intField', default=Struct(fmt='>h'))}])}]), 'spawn_entity_living': Container(fields=[{'name': 'entityId', 'type': VarInt(bits=32)}, {'name': 'type', 'type': Struct(fmt='B')}, {'name': 'x', 'type': Struct(fmt='>i')}, {'name': 'y', 'type': Struct(fmt='>i')}, {'name': 'z', 'type': Struct(fmt='>i')}, {'name': 'yaw', 'type': Struct(fmt='b')}, {'name': 'pitch', 'type': Struct(fmt='b')}, {'name': 'headPitch', 'type': Struct(fmt='b')}, {'name': 'velocityX', 'type': Struct(fmt='>h')}, {'name': 'velocityY', 'type': Struct(fmt='>h')}, {'name': 'velocityZ', 'type': Struct(fmt='>h')}, {'name': 'metadata', 'type': EntityMetadataArray(type=Switch(fields={'0': Struct(fmt='b'), '1': Struct(fmt='>h'), '2': Struct(fmt='>i'), '3': Struct(fmt='>f'), '4': String(countType=VarInt(bits=32)), '5': Container(fields=[{'name': 'blockId', 'type': Struct(fmt='>h')}, {'anon': True, 'type': Switch(fields={'-1': Void()}, compareTo='blockId', default=Container(fields=[{'name': 'itemCount', 'type': Struct(fmt='b')}, {'name': 'itemDamage', 'type': Struct(fmt='>h')}, {'name': 'nbtData', 'type': NBT()}]))}]), '6': Container(fields=[{'name': 'x', 'type': Struct(fmt='>i')}, {'name': 'y', 'type': Struct(fmt='>i')}, {'name': 'z', 'type': Struct(fmt='>i')}]), '7': Container(fields=[{'name': 'pitch', 'type': Struct(fmt='>f')}, {'name': 'yaw', 'type': Struct(fmt='>f')}, {'name': 'roll', 'type': Struct(fmt='>f')}])}, compareTo='type', default=None), endVal=127)}]), 'spawn_entity_painting': Container(fields=[{'name': 'entityId', 'type': VarInt(bits=32)}, {'name': 'title', 'type': String(countType=VarInt(bits=32))}, {'name': 'location', 'type': Container(fields=[{'name': 'x', 'type': Struct(fmt='>i')}, {'name': 'y', 'type': Struct(fmt='>i')}, {'name': 'z', 'type': Struct(fmt='>i')}])}, {'name': 'direction', 'type': Struct(fmt='B')}]), 'spawn_entity_experience_orb': Container(fields=[{'name': 'entityId', 'type': VarInt(bits=32)}, {'name': 'x', 'type': Struct(fmt='>i')}, {'name': 'y', 'type': Struct(fmt='>i')}, {'name': 'z', 'type': Struct(fmt='>i')}, {'name': 'count', 'type': Struct(fmt='>h')}]), 'entity_velocity': Container(fields=[{'name': 'entityId', 'type': Struct(fmt='>i')}, {'name': 'velocityX', 'type': Struct(fmt='>h')}, {'name': 'velocityY', 'type': Struct(fmt='>h')}, {'name': 'velocityZ', 'type': Struct(fmt='>h')}]), 'entity_destroy': Container(fields=[{'name': 'entityIds', 'type': Array(type=Struct(fmt='>i'), count=None, countType=Struct(fmt='b'))}]), 'entity': Container(fields=[{'name': 'entityId', 'type': Struct(fmt='>i')}]), 'rel_entity_move': Container(fields=[{'name': 'entityId', 'type': Struct(fmt='>i')}, {'name': 'dX', 'type': Struct(fmt='b')}, {'name': 'dY', 'type': Struct(fmt='b')}, {'name': 'dZ', 'type': Struct(fmt='b')}]), 'entity_look': Container(fields=[{'name': 'entityId', 'type': Struct(fmt='>i')}, {'name': 'yaw', 'type': Struct(fmt='b')}, {'name': 'pitch', 'type': Struct(fmt='b')}]), 'entity_move_look': Container(fields=[{'name': 'entityId', 'type': Struct(fmt='>i')}, {'name': 'dX', 'type': Struct(fmt='b')}, {'name': 'dY', 'type': Struct(fmt='b')}, {'name': 'dZ', 'type': Struct(fmt='b')}, {'name': 'yaw', 'type': Struct(fmt='b')}, {'name': 'pitch', 'type': Struct(fmt='b')}]), 'entity_teleport': Container(fields=[{'name': 'entityId', 'type': Struct(fmt='>i')}, {'name': 'x', 'type': Struct(fmt='>i')}, {'name': 'y', 'type': Struct(fmt='>i')}, {'name': 'z', 'type': Struct(fmt='>i')}, {'name': 'yaw', 'type': Struct(fmt='b')}, {'name': 'pitch', 'type': Struct(fmt='b')}]), 'entity_head_rotation': Container(fields=[{'name': 'entityId', 'type': Struct(fmt='>i')}, {'name': 'headYaw', 'type': Struct(fmt='b')}]), 'entity_status': Container(fields=[{'name': 'entityId', 'type': Struct(fmt='>i')}, {'name': 'entityStatus', 'type': Struct(fmt='b')}]), 'attach_entity': Container(fields=[{'name': 'entityId', 'type': Struct(fmt='>i')}, {'name': 'vehicleId', 'type': Struct(fmt='>i')}, {'name': 'leash', 'type': Struct(fmt='?')}]), 'entity_metadata': Container(fields=[{'name': 'entityId', 'type': Struct(fmt='>i')}, {'name': 'metadata', 'type': EntityMetadataArray(type=Switch(fields={'0': Struct(fmt='b'), '1': Struct(fmt='>h'), '2': Struct(fmt='>i'), '3': Struct(fmt='>f'), '4': String(countType=VarInt(bits=32)), '5': Container(fields=[{'name': 'blockId', 'type': Struct(fmt='>h')}, {'anon': True, 'type': Switch(fields={'-1': Void()}, compareTo='blockId', default=Container(fields=[{'name': 'itemCount', 'type': Struct(fmt='b')}, {'name': 'itemDamage', 'type': Struct(fmt='>h')}, {'name': 'nbtData', 'type': NBT()}]))}]), '6': Container(fields=[{'name': 'x', 'type': Struct(fmt='>i')}, {'name': 'y', 'type': Struct(fmt='>i')}, {'name': 'z', 'type': Struct(fmt='>i')}]), '7': Container(fields=[{'name': 'pitch', 'type': Struct(fmt='>f')}, {'name': 'yaw', 'type': Struct(fmt='>f')}, {'name': 'roll', 'type': Struct(fmt='>f')}])}, compareTo='type', default=None), endVal=127)}]), 'entity_effect': Container(fields=[{'name': 'entityId', 'type': Struct(fmt='>i')}, {'name': 'effectId', 'type': Struct(fmt='b')}, {'name': 'amplifier', 'type': Struct(fmt='b')}, {'name': 'duration', 'type': Struct(fmt='>h')}]), 'remove_entity_effect': Container(fields=[{'name': 'entityId', 'type': Struct(fmt='>i')}, {'name': 'effectId', 'type': Struct(fmt='b')}]), 'experience': Container(fields=[{'name': 'experienceBar', 'type': Struct(fmt='>f')}, {'name': 'level', 'type': Struct(fmt='>h')}, {'name': 'totalExperience', 'type': Struct(fmt='>h')}]), 'update_attributes': Container(fields=[{'name': 'entityId', 'type': Struct(fmt='>i')}, {'name': 'properties', 'type': Array(type=Container(fields=[{'name': 'key', 'type': String(countType=VarInt(bits=32))}, {'name': 'value', 'type': Struct(fmt='>d')}, {'name': 'modifiers', 'type': Array(type=Container(fields=[{'name': 'UUID', 'type': UUID()}, {'name': 'amount', 'type': Struct(fmt='>d')}, {'name': 'operation', 'type': Struct(fmt='b')}]), count=None, countType=Struct(fmt='>h'))}]), count=None, countType=Struct(fmt='>i'))}]), 'map_chunk': Container(fields=[{'name': 'x', 'type': Struct(fmt='>i')}, {'name': 'z', 'type': Struct(fmt='>i')}, {'name': 'groundUp', 'type': Struct(fmt='?')}, {'name': 'bitMap', 'type': Struct(fmt='>H')}, {'name': 'addBitMap', 'type': Struct(fmt='>H')}, {'name': 'compressedChunkData', 'type': ByteArray(count=None, countType=Struct(fmt='>i'))}]), 'multi_block_change': Container(fields=[{'name': 'chunkX', 'type': Struct(fmt='>i')}, {'name': 'chunkZ', 'type': Struct(fmt='>i')}, {'name': 'recordCount', 'type': Count(type=Struct(fmt='>h'), countFor='records')}, {'name': 'dataLength', 'type': Struct(fmt='>i')}, {'name': 'records', 'type': Array(type=Container(fields=[{'anon': True, 'type': BitField(fields=[{'name': 'metadata', 'size': 4, 'signed': False}, {'name': 'blockId', 'size': 12, 'signed': False}])}, {'name': 'y', 'type': Struct(fmt='B')}, {'anon': True, 'type': BitField(fields=[{'name': 'z', 'size': 4, 'signed': False}, {'name': 'x', 'size': 4, 'signed': False}])}]), count='recordCount', countType=None)}]), 'block_change': Container(fields=[{'name': 'location', 'type': Container(fields=[{'name': 'x', 'type': Struct(fmt='>i')}, {'name': 'y', 'type': Struct(fmt='B')}, {'name': 'z', 'type': Struct(fmt='>i')}])}, {'name': 'type', 'type': VarInt(bits=32)}, {'name': 'metadata', 'type': Struct(fmt='B')}]), 'block_action': Container(fields=[{'name': 'location', 'type': Container(fields=[{'name': 'x', 'type': Struct(fmt='>i')}, {'name': 'y', 'type': Struct(fmt='>h')}, {'name': 'z', 'type': Struct(fmt='>i')}])}, {'name': 'byte1', 'type': Struct(fmt='B')}, {'name': 'byte2', 'type': Struct(fmt='B')}, {'name': 'blockId', 'type': VarInt(bits=32)}]), 'block_break_animation': Container(fields=[{'name': 'entityId', 'type': VarInt(bits=32)}, {'name': 'location', 'type': Container(fields=[{'name': 'x', 'type': Struct(fmt='>i')}, {'name': 'y', 'type': Struct(fmt='>i')}, {'name': 'z', 'type': Struct(fmt='>i')}])}, {'name': 'destroyStage', 'type': Struct(fmt='b')}]), 'map_chunk_bulk': Container(fields=[{'name': 'chunkColumnCount', 'type': Count(type=Struct(fmt='>h'), countFor='meta')}, {'name': 'dataLength', 'type': Count(type=Struct(fmt='>i'), countFor='compressedChunkData')}, {'name': 'skyLightSent', 'type': Struct(fmt='?')}, {'name': 'compressedChunkData', 'type': ByteArray(count='dataLength', countType=None)}, {'name': 'meta', 'type': Array(type=Container(fields=[{'name': 'x', 'type': Struct(fmt='>i')}, {'name': 'z', 'type': Struct(fmt='>i')}, {'name': 'bitMap', 'type': Struct(fmt='>H')}, {'name': 'addBitMap', 'type': Struct(fmt='>H')}]), count='chunkColumnCount', countType=None)}]), 'explosion': Container(fields=[{'name': 'x', 'type': Struct(fmt='>f')}, {'name': 'y', 'type': Struct(fmt='>f')}, {'name': 'z', 'type': Struct(fmt='>f')}, {'name': 'radius', 'type': Struct(fmt='>f')}, {'name': 'affectedBlockOffsets', 'type': Array(type=Container(fields=[{'name': 'x', 'type': Struct(fmt='b')}, {'name': 'y', 'type': Struct(fmt='b')}, {'name': 'z', 'type': Struct(fmt='b')}]), count=None, countType=Struct(fmt='>i'))}, {'name': 'playerMotionX', 'type': Struct(fmt='>f')}, {'name': 'playerMotionY', 'type': Struct(fmt='>f')}, {'name': 'playerMotionZ', 'type': Struct(fmt='>f')}]), 'world_event': Container(fields=[{'name': 'effectId', 'type': Struct(fmt='>i')}, {'name': 'location', 'type': Container(fields=[{'name': 'x', 'type': Struct(fmt='>i')}, {'name': 'y', 'type': Struct(fmt='B')}, {'name': 'z', 'type': Struct(fmt='>i')}])}, {'name': 'data', 'type': Struct(fmt='>i')}, {'name': 'global', 'type': Struct(fmt='?')}]), 'named_sound_effect': Container(fields=[{'name': 'soundName', 'type': String(countType=VarInt(bits=32))}, {'name': 'x', 'type': Struct(fmt='>i')}, {'name': 'y', 'type': Struct(fmt='>i')}, {'name': 'z', 'type': Struct(fmt='>i')}, {'name': 'volume', 'type': Struct(fmt='>f')}, {'name': 'pitch', 'type': Struct(fmt='B')}]), 'world_particles': Container(fields=[{'name': 'particleName', 'type': String(countType=VarInt(bits=32))}, {'name': 'x', 'type': Struct(fmt='>f')}, {'name': 'y', 'type': Struct(fmt='>f')}, {'name': 'z', 'type': Struct(fmt='>f')}, {'name': 'offsetX', 'type': Struct(fmt='>f')}, {'name': 'offsetY', 'type': Struct(fmt='>f')}, {'name': 'offsetZ', 'type': Struct(fmt='>f')}, {'name': 'particleData', 'type': Struct(fmt='>f')}, {'name': 'particles', 'type': Struct(fmt='>i')}]), 'game_state_change': Container(fields=[{'name': 'reason', 'type': Struct(fmt='B')}, {'name': 'gameMode', 'type': Struct(fmt='>f')}]), 'spawn_entity_weather': Container(fields=[{'name': 'entityId', 'type': VarInt(bits=32)}, {'name': 'type', 'type': Struct(fmt='b')}, {'name': 'x', 'type': Struct(fmt='>i')}, {'name': 'y', 'type': Struct(fmt='>i')}, {'name': 'z', 'type': Struct(fmt='>i')}]), 'open_window': Container(fields=[{'name': 'windowId', 'type': Struct(fmt='B')}, {'name': 'inventoryType', 'type': Struct(fmt='B')}, {'name': 'windowTitle', 'type': String(countType=VarInt(bits=32))}, {'name': 'slotCount', 'type': Struct(fmt='B')}, {'name': 'useProvidedTitle', 'type': Struct(fmt='?')}, {'name': 'entityId', 'type': Switch(fields={'EntityHorse': Struct(fmt='>i')}, compareTo='inventoryType', default=Void())}]), 'close_window': Container(fields=[{'name': 'windowId', 'type': Struct(fmt='B')}]), 'set_slot': Container(fields=[{'name': 'windowId', 'type': Struct(fmt='b')}, {'name': 'slot', 'type': Struct(fmt='>h')}, {'name': 'item', 'type': Container(fields=[{'name': 'blockId', 'type': Struct(fmt='>h')}, {'anon': True, 'type': Switch(fields={'-1': Void()}, compareTo='blockId', default=Container(fields=[{'name': 'itemCount', 'type': Struct(fmt='b')}, {'name': 'itemDamage', 'type': Struct(fmt='>h')}, {'name': 'nbtData', 'type': NBT()}]))}])}]), 'window_items': Container(fields=[{'name': 'windowId', 'type': Struct(fmt='B')}, {'name': 'items', 'type': Array(type=Container(fields=[{'name': 'blockId', 'type': Struct(fmt='>h')}, {'anon': True, 'type': Switch(fields={'-1': Void()}, compareTo='blockId', default=Container(fields=[{'name': 'itemCount', 'type': Struct(fmt='b')}, {'name': 'itemDamage', 'type': Struct(fmt='>h')}, {'name': 'nbtData', 'type': NBT()}]))}]), count=None, countType=Struct(fmt='>h'))}]), 'craft_progress_bar': Container(fields=[{'name': 'windowId', 'type': Struct(fmt='B')}, {'name': 'property', 'type': Struct(fmt='>h')}, {'name': 'value', 'type': Struct(fmt='>h')}]), 'transaction': Container(fields=[{'name': 'windowId', 'type': Struct(fmt='B')}, {'name': 'action', 'type': Struct(fmt='>h')}, {'name': 'accepted', 'type': Struct(fmt='?')}]), 'update_sign': Container(fields=[{'name': 'location', 'type': Container(fields=[{'name': 'x', 'type': Struct(fmt='>i')}, {'name': 'y', 'type': Struct(fmt='>h')}, {'name': 'z', 'type': Struct(fmt='>i')}])}, {'name': 'text1', 'type': String(countType=VarInt(bits=32))}, {'name': 'text2', 'type': String(countType=VarInt(bits=32))}, {'name': 'text3', 'type': String(countType=VarInt(bits=32))}, {'name': 'text4', 'type': String(countType=VarInt(bits=32))}]), 'map': Container(fields=[{'name': 'itemDamage', 'type': VarInt(bits=32)}, {'name': 'data', 'type': ByteArray(count=None, countType=Struct(fmt='>h'))}]), 'tile_entity_data': Container(fields=[{'name': 'location', 'type': Container(fields=[{'name': 'x', 'type': Struct(fmt='>i')}, {'name': 'y', 'type': Struct(fmt='>h')}, {'name': 'z', 'type': Struct(fmt='>i')}])}, {'name': 'action', 'type': Struct(fmt='B')}, {'name': 'nbtData', 'type': NBT()}]), 'open_sign_entity': Container(fields=[{'name': 'location', 'type': Container(fields=[{'name': 'x', 'type': Struct(fmt='>i')}, {'name': 'y', 'type': Struct(fmt='>i')}, {'name': 'z', 'type': Struct(fmt='>i')}])}]), 'statistics': Container(fields=[{'name': 'entries', 'type': Array(type=Container(fields=[{'name': 'name', 'type': String(countType=VarInt(bits=32))}, {'name': 'value', 'type': VarInt(bits=32)}]), count=None, countType=VarInt(bits=32))}]), 'player_info': Container(fields=[{'name': 'playerName', 'type': String(countType=VarInt(bits=32))}, {'name': 'online', 'type': Struct(fmt='?')}, {'name': 'ping', 'type': Struct(fmt='>h')}]), 'abilities': Container(fields=[{'name': 'flags', 'type': Struct(fmt='b')}, {'name': 'flyingSpeed', 'type': Struct(fmt='>f')}, {'name': 'walkingSpeed', 'type': Struct(fmt='>f')}]), 'tab_complete': Container(fields=[{'name': 'matches', 'type': Array(type=String(countType=VarInt(bits=32)), count=None, countType=VarInt(bits=32))}]), 'scoreboard_objective': Container(fields=[{'name': 'name', 'type': String(countType=VarInt(bits=32))}, {'name': 'displayText', 'type': String(countType=VarInt(bits=32))}, {'name': 'action', 'type': Struct(fmt='b')}]), 'scoreboard_score': Container(fields=[{'name': 'itemName', 'type': String(countType=VarInt(bits=32))}, {'name': 'action', 'type': Struct(fmt='b')}, {'name': 'scoreName', 'type': String(countType=VarInt(bits=32))}, {'name': 'value', 'type': Switch(fields={'1': Void()}, compareTo='action', default=Struct(fmt='>i'))}]), 'scoreboard_display_objective': Container(fields=[{'name': 'position', 'type': Struct(fmt='b')}, {'name': 'name', 'type': String(countType=VarInt(bits=32))}]), 'scoreboard_team': Container(fields=[{'name': 'team', 'type': String(countType=VarInt(bits=32))}, {'name': 'mode', 'type': Struct(fmt='b')}, {'name': 'name', 'type': Switch(fields={'0': String(countType=VarInt(bits=32)), '2': String(countType=VarInt(bits=32))}, compareTo='mode', default=Void())}, {'name': 'prefix', 'type': Switch(fields={'0': String(countType=VarInt(bits=32)), '2': String(countType=VarInt(bits=32))}, compareTo='mode', default=Void())}, {'name': 'suffix', 'type': Switch(fields={'0': String(countType=VarInt(bits=32)), '2': String(countType=VarInt(bits=32))}, compareTo='mode', default=Void())}, {'name': 'friendlyFire', 'type': Switch(fields={'0': Struct(fmt='b'), '2': Struct(fmt='b')}, compareTo='mode', default=Void())}, {'name': 'nameTagVisibility', 'type': Switch(fields={'0': String(countType=VarInt(bits=32)), '2': String(countType=VarInt(bits=32))}, compareTo='mode', default=Void())}, {'name': 'color', 'type': Switch(fields={'0': Struct(fmt='b'), '2': Struct(fmt='b')}, compareTo='mode', default=Void())}, {'name': 'players', 'type': Switch(fields={'0': Array(type=String(countType=VarInt(bits=32)), count=None, countType=Struct(fmt='>h')), '3': Array(type=String(countType=VarInt(bits=32)), count=None, countType=VarInt(bits=32)), '4': Array(type=String(countType=VarInt(bits=32)), count=None, countType=VarInt(bits=32))}, compareTo='mode', default=Void())}]), 'custom_payload': Container(fields=[{'name': 'channel', 'type': String(countType=VarInt(bits=32))}, {'name': 'data', 'type': ByteArray(count=None, countType=Struct(fmt='>h'))}]), 'kick_disconnect': Container(fields=[{'name': 'reason', 'type': String(countType=VarInt(bits=32))}])}, compareTo='name', default=None)}])
packet_play_up = Container(fields=[{'name': 'name', 'type': Mapper(type=VarInt(bits=32), mappings={'0x00': 'keep_alive', '0x01': 'chat', '0x02': 'use_entity', '0x03': 'flying', '0x04': 'position', '0x05': 'look', '0x06': 'position_look', '0x07': 'block_dig', '0x08': 'block_place', '0x09': 'held_item_slot', '0x0a': 'arm_animation', '0x0b': 'entity_action', '0x0c': 'steer_vehicle', '0x0d': 'close_window', '0x0e': 'window_click', '0x0f': 'transaction', '0x10': 'set_creative_slot', '0x11': 'enchant_item', '0x12': 'update_sign', '0x13': 'abilities', '0x14': 'tab_complete', '0x15': 'settings', '0x16': 'client_command', '0x17': 'custom_payload'})}, {'name': 'params', 'type': Switch(fields={'keep_alive': Container(fields=[{'name': 'keepAliveId', 'type': Struct(fmt='>i')}]), 'chat': Container(fields=[{'name': 'message', 'type': String(countType=VarInt(bits=32))}]), 'use_entity': Container(fields=[{'name': 'target', 'type': Struct(fmt='>i')}, {'name': 'mouse', 'type': Struct(fmt='b')}, {'name': 'x', 'type': Switch(fields={'2': Struct(fmt='>f')}, compareTo='mouse', default=Void())}, {'name': 'y', 'type': Switch(fields={'2': Struct(fmt='>f')}, compareTo='mouse', default=Void())}, {'name': 'z', 'type': Switch(fields={'2': Struct(fmt='>f')}, compareTo='mouse', default=Void())}]), 'flying': Container(fields=[{'name': 'onGround', 'type': Struct(fmt='?')}]), 'position': Container(fields=[{'name': 'x', 'type': Struct(fmt='>d')}, {'name': 'stance', 'type': Struct(fmt='>d')}, {'name': 'y', 'type': Struct(fmt='>d')}, {'name': 'z', 'type': Struct(fmt='>d')}, {'name': 'onGround', 'type': Struct(fmt='?')}]), 'look': Container(fields=[{'name': 'yaw', 'type': Struct(fmt='>f')}, {'name': 'pitch', 'type': Struct(fmt='>f')}, {'name': 'onGround', 'type': Struct(fmt='?')}]), 'position_look': Container(fields=[{'name': 'x', 'type': Struct(fmt='>d')}, {'name': 'stance', 'type': Struct(fmt='>d')}, {'name': 'y', 'type': Struct(fmt='>d')}, {'name': 'z', 'type': Struct(fmt='>d')}, {'name': 'yaw', 'type': Struct(fmt='>f')}, {'name': 'pitch', 'type': Struct(fmt='>f')}, {'name': 'onGround', 'type': Struct(fmt='?')}]), 'block_dig': Container(fields=[{'name': 'status', 'type': Struct(fmt='b')}, {'name': 'location', 'type': Container(fields=[{'name': 'x', 'type': Struct(fmt='>i')}, {'name': 'y', 'type': Struct(fmt='B')}, {'name': 'z', 'type': Struct(fmt='>i')}])}, {'name': 'face', 'type': Struct(fmt='b')}]), 'block_place': Container(fields=[{'name': 'location', 'type': Container(fields=[{'name': 'x', 'type': Struct(fmt='>i')}, {'name': 'y', 'type': Struct(fmt='B')}, {'name': 'z', 'type': Struct(fmt='>i')}])}, {'name': 'direction', 'type': Struct(fmt='b')}, {'name': 'heldItem', 'type': Container(fields=[{'name': 'blockId', 'type': Struct(fmt='>h')}, {'anon': True, 'type': Switch(fields={'-1': Void()}, compareTo='blockId', default=Container(fields=[{'name': 'itemCount', 'type': Struct(fmt='b')}, {'name': 'itemDamage', 'type': Struct(fmt='>h')}, {'name': 'nbtData', 'type': NBT()}]))}])}, {'name': 'cursorX', 'type': Struct(fmt='b')}, {'name': 'cursorY', 'type': Struct(fmt='b')}, {'name': 'cursorZ', 'type': Struct(fmt='b')}]), 'held_item_slot': Container(fields=[{'name': 'slotId', 'type': Struct(fmt='>h')}]), 'arm_animation': Container(fields=[{'name': 'entityId', 'type': Struct(fmt='>i')}, {'name': 'animation', 'type': Struct(fmt='b')}]), 'entity_action': Container(fields=[{'name': 'entityId', 'type': Struct(fmt='>i')}, {'name': 'actionId', 'type': Struct(fmt='b')}, {'name': 'jumpBoost', 'type': Struct(fmt='>i')}]), 'steer_vehicle': Container(fields=[{'name': 'sideways', 'type': Struct(fmt='>f')}, {'name': 'forward', 'type': Struct(fmt='>f')}, {'name': 'jump', 'type': Struct(fmt='?')}, {'name': 'unmount', 'type': Struct(fmt='?')}]), 'close_window': Container(fields=[{'name': 'windowId', 'type': Struct(fmt='B')}]), 'window_click': Container(fields=[{'name': 'windowId', 'type': Struct(fmt='b')}, {'name': 'slot', 'type': Struct(fmt='>h')}, {'name': 'mouseButton', 'type': Struct(fmt='b')}, {'name': 'action', 'type': Struct(fmt='>h')}, {'name': 'mode', 'type': Struct(fmt='b')}, {'name': 'item', 'type': Container(fields=[{'name': 'blockId', 'type': Struct(fmt='>h')}, {'anon': True, 'type': Switch(fields={'-1': Void()}, compareTo='blockId', default=Container(fields=[{'name': 'itemCount', 'type': Struct(fmt='b')}, {'name': 'itemDamage', 'type': Struct(fmt='>h')}, {'name': 'nbtData', 'type': NBT()}]))}])}]), 'transaction': Container(fields=[{'name': 'windowId', 'type': Struct(fmt='b')}, {'name': 'action', 'type': Struct(fmt='>h')}, {'name': 'accepted', 'type': Struct(fmt='?')}]), 'set_creative_slot': Container(fields=[{'name': 'slot', 'type': Struct(fmt='>h')}, {'name': 'item', 'type': Container(fields=[{'name': 'blockId', 'type': Struct(fmt='>h')}, {'anon': True, 'type': Switch(fields={'-1': Void()}, compareTo='blockId', default=Container(fields=[{'name': 'itemCount', 'type': Struct(fmt='b')}, {'name': 'itemDamage', 'type': Struct(fmt='>h')}, {'name': 'nbtData', 'type': NBT()}]))}])}]), 'enchant_item': Container(fields=[{'name': 'windowId', 'type': Struct(fmt='b')}, {'name': 'enchantment', 'type': Struct(fmt='b')}]), 'update_sign': Container(fields=[{'name': 'location', 'type': Container(fields=[{'name': 'x', 'type': Struct(fmt='>i')}, {'name': 'y', 'type': Struct(fmt='>h')}, {'name': 'z', 'type': Struct(fmt='>i')}])}, {'name': 'text1', 'type': String(countType=VarInt(bits=32))}, {'name': 'text2', 'type': String(countType=VarInt(bits=32))}, {'name': 'text3', 'type': String(countType=VarInt(bits=32))}, {'name': 'text4', 'type': String(countType=VarInt(bits=32))}]), 'abilities': Container(fields=[{'name': 'flags', 'type': Struct(fmt='b')}, {'name': 'flyingSpeed', 'type': Struct(fmt='>f')}, {'name': 'walkingSpeed', 'type': Struct(fmt='>f')}]), 'tab_complete': Container(fields=[{'name': 'text', 'type': String(countType=VarInt(bits=32))}]), 'settings': Container(fields=[{'name': 'locale', 'type': String(countType=VarInt(bits=32))}, {'name': 'viewDistance', 'type': Struct(fmt='b')}, {'name': 'chatFlags', 'type': Struct(fmt='b')}, {'name': 'chatColors', 'type': Struct(fmt='?')}, {'name': 'difficulty', 'type': Struct(fmt='B')}, {'name': 'showCape', 'type': Struct(fmt='?')}]), 'client_command': Container(fields=[{'name': 'payload', 'type': Struct(fmt='b')}]), 'custom_payload': Container(fields=[{'name': 'channel', 'type': String(countType=VarInt(bits=32))}, {'name': 'data', 'type': ByteArray(count=None, countType=Struct(fmt='>h'))}])}, compareTo='name', default=None)}])
