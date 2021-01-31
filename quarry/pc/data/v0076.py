# !!! auto-generated - do not edit !!!
from quarry.native import *
edition = 'pc'
release = '15w40b'
version = 76
packet_init_down = Container(fields=[{'name': 'name', 'type': Mapper(type=VarInt(bits=32), mappings={})}, {'name': 'params', 'type': Switch(fields={}, compareTo='name', default=None)}])
packet_init_up = Container(fields=[{'name': 'name', 'type': Mapper(type=VarInt(bits=32), mappings={'0x00': 'set_protocol', '0xfe': 'legacy_server_list_ping'})}, {'name': 'params', 'type': Switch(fields={'set_protocol': Container(fields=[{'name': 'protocolVersion', 'type': VarInt(bits=32)}, {'name': 'serverHost', 'type': String(countType=VarInt(bits=32))}, {'name': 'serverPort', 'type': Struct(fmt='>H')}, {'name': 'nextState', 'type': VarInt(bits=32)}]), 'legacy_server_list_ping': Container(fields=[{'name': 'payload', 'type': Struct(fmt='B')}])}, compareTo='name', default=None)}])
packet_status_down = Container(fields=[{'name': 'name', 'type': Mapper(type=VarInt(bits=32), mappings={'0x00': 'server_info', '0x01': 'ping'})}, {'name': 'params', 'type': Switch(fields={'server_info': Container(fields=[{'name': 'response', 'type': String(countType=VarInt(bits=32))}]), 'ping': Container(fields=[{'name': 'time', 'type': Struct(fmt='>q')}])}, compareTo='name', default=None)}])
packet_status_up = Container(fields=[{'name': 'name', 'type': Mapper(type=VarInt(bits=32), mappings={'0x00': 'ping_start', '0x01': 'ping'})}, {'name': 'params', 'type': Switch(fields={'ping_start': Container(fields=[]), 'ping': Container(fields=[{'name': 'time', 'type': Struct(fmt='>q')}])}, compareTo='name', default=None)}])
packet_login_down = Container(fields=[{'name': 'name', 'type': Mapper(type=VarInt(bits=32), mappings={'0x00': 'disconnect', '0x01': 'encryption_begin', '0x02': 'success', '0x03': 'compress'})}, {'name': 'params', 'type': Switch(fields={'disconnect': Container(fields=[{'name': 'reason', 'type': String(countType=VarInt(bits=32))}]), 'encryption_begin': Container(fields=[{'name': 'serverId', 'type': String(countType=VarInt(bits=32))}, {'name': 'publicKey', 'type': ByteArray(count=None, countType=VarInt(bits=32))}, {'name': 'verifyToken', 'type': ByteArray(count=None, countType=VarInt(bits=32))}]), 'success': Container(fields=[{'name': 'uuid', 'type': String(countType=VarInt(bits=32))}, {'name': 'username', 'type': String(countType=VarInt(bits=32))}]), 'compress': Container(fields=[{'name': 'threshold', 'type': VarInt(bits=32)}])}, compareTo='name', default=None)}])
packet_login_up = Container(fields=[{'name': 'name', 'type': Mapper(type=VarInt(bits=32), mappings={'0x00': 'login_start', '0x01': 'encryption_begin'})}, {'name': 'params', 'type': Switch(fields={'login_start': Container(fields=[{'name': 'username', 'type': String(countType=VarInt(bits=32))}]), 'encryption_begin': Container(fields=[{'name': 'sharedSecret', 'type': ByteArray(count=None, countType=VarInt(bits=32))}, {'name': 'verifyToken', 'type': ByteArray(count=None, countType=VarInt(bits=32))}])}, compareTo='name', default=None)}])
packet_play_down = Container(fields=[{'name': 'name', 'type': Mapper(type=VarInt(bits=32), mappings={'0x1f': 'keep_alive', '0x24': 'login', '0x0f': 'chat', '0x43': 'update_time', '0x3c': 'entity_equipment', '0x42': 'spawn_position', '0x3e': 'update_health', '0x33': 'respawn', '0x2e': 'position', '0x37': 'held_item_slot', '0x2f': 'bed', '0x06': 'animation', '0x05': 'named_entity_spawn', '0x47': 'collect', '0x00': 'spawn_entity', '0x03': 'spawn_entity_living', '0x04': 'spawn_entity_painting', '0x01': 'spawn_entity_experience_orb', '0x3b': 'entity_velocity', '0x30': 'entity_destroy', '0x29': 'entity', '0x26': 'rel_entity_move', '0x28': 'entity_look', '0x27': 'entity_move_look', '0x48': 'entity_teleport', '0x34': 'entity_head_rotation', '0x1a': 'entity_status', '0x3a': 'attach_entity', '0x39': 'entity_metadata', '0x4a': 'entity_effect', '0x31': 'remove_entity_effect', '0x3d': 'experience', '0x49': 'update_attributes', '0x20': 'map_chunk', '0x10': 'multi_block_change', '0x0b': 'block_change', '0x0a': 'block_action', '0x08': 'block_break_animation', '0x1b': 'explosion', '0x21': 'world_event', '0x23': 'named_sound_effect', '0x22': 'world_particles', '0x1e': 'game_state_change', '0x02': 'spawn_entity_weather', '0x13': 'open_window', '0x12': 'close_window', '0x16': 'set_slot', '0x14': 'window_items', '0x15': 'craft_progress_bar', '0x11': 'transaction', '0x45': 'update_sign', '0x25': 'map', '0x09': 'tile_entity_data', '0x2a': 'open_sign_entity', '0x07': 'statistics', '0x2d': 'player_info', '0x2b': 'abilities', '0x0e': 'tab_complete', '0x3f': 'scoreboard_objective', '0x41': 'scoreboard_score', '0x38': 'scoreboard_display_objective', '0x40': 'scoreboard_team', '0x18': 'custom_payload', '0x19': 'kick_disconnect', '0x0d': 'difficulty', '0x2c': 'combat_event', '0x36': 'camera', '0x35': 'world_border', '0x44': 'title', '0x1d': 'set_compression', '0x46': 'playerlist_header', '0x32': 'resource_pack_send', '0x0c': 'boss_bar', '0x17': 'set_cooldown', '0x1c': 'unload_chunk'})}, {'name': 'params', 'type': Switch(fields={'keep_alive': Container(fields=[{'name': 'keepAliveId', 'type': VarInt(bits=32)}]), 'login': Container(fields=[{'name': 'entityId', 'type': Struct(fmt='>i')}, {'name': 'gameMode', 'type': Struct(fmt='B')}, {'name': 'dimension', 'type': Struct(fmt='b')}, {'name': 'difficulty', 'type': Struct(fmt='B')}, {'name': 'maxPlayers', 'type': Struct(fmt='B')}, {'name': 'levelType', 'type': String(countType=VarInt(bits=32))}, {'name': 'reducedDebugInfo', 'type': Struct(fmt='?')}]), 'chat': Container(fields=[{'name': 'message', 'type': String(countType=VarInt(bits=32))}, {'name': 'position', 'type': Struct(fmt='b')}]), 'update_time': Container(fields=[{'name': 'age', 'type': Struct(fmt='>q')}, {'name': 'time', 'type': Struct(fmt='>q')}]), 'entity_equipment': Container(fields=[{'name': 'entityId', 'type': VarInt(bits=32)}, {'name': 'slot', 'type': VarInt(bits=32)}, {'name': 'item', 'type': Container(fields=[{'name': 'blockId', 'type': Struct(fmt='>h')}, {'anon': True, 'type': Switch(fields={'-1': Void()}, compareTo='blockId', default=Container(fields=[{'name': 'itemCount', 'type': Struct(fmt='b')}, {'name': 'itemDamage', 'type': Struct(fmt='>h')}, {'name': 'nbtData', 'type': NBT()}]))}])}]), 'spawn_position': Container(fields=[{'name': 'location', 'type': BitField(fields=[{'name': 'x', 'size': 26, 'signed': True}, {'name': 'y', 'size': 12, 'signed': True}, {'name': 'z', 'size': 26, 'signed': True}])}]), 'update_health': Container(fields=[{'name': 'health', 'type': Struct(fmt='>f')}, {'name': 'food', 'type': VarInt(bits=32)}, {'name': 'foodSaturation', 'type': Struct(fmt='>f')}]), 'respawn': Container(fields=[{'name': 'dimension', 'type': Struct(fmt='>i')}, {'name': 'difficulty', 'type': Struct(fmt='B')}, {'name': 'gamemode', 'type': Struct(fmt='B')}, {'name': 'levelType', 'type': String(countType=VarInt(bits=32))}]), 'position': Container(fields=[{'name': 'x', 'type': Struct(fmt='>d')}, {'name': 'y', 'type': Struct(fmt='>d')}, {'name': 'z', 'type': Struct(fmt='>d')}, {'name': 'yaw', 'type': Struct(fmt='>f')}, {'name': 'pitch', 'type': Struct(fmt='>f')}, {'name': 'flags', 'type': Struct(fmt='b')}]), 'held_item_slot': Container(fields=[{'name': 'slot', 'type': Struct(fmt='b')}]), 'bed': Container(fields=[{'name': 'entityId', 'type': VarInt(bits=32)}, {'name': 'location', 'type': BitField(fields=[{'name': 'x', 'size': 26, 'signed': True}, {'name': 'y', 'size': 12, 'signed': True}, {'name': 'z', 'size': 26, 'signed': True}])}]), 'animation': Container(fields=[{'name': 'entityId', 'type': VarInt(bits=32)}, {'name': 'animation', 'type': Struct(fmt='B')}]), 'named_entity_spawn': Container(fields=[{'name': 'entityId', 'type': VarInt(bits=32)}, {'name': 'playerUUID', 'type': UUID()}, {'name': 'x', 'type': Struct(fmt='>i')}, {'name': 'y', 'type': Struct(fmt='>i')}, {'name': 'z', 'type': Struct(fmt='>i')}, {'name': 'yaw', 'type': Struct(fmt='b')}, {'name': 'pitch', 'type': Struct(fmt='b')}, {'name': 'metadata', 'type': EntityMetadataArray(type=Switch(fields={'0': Struct(fmt='b'), '1': VarInt(bits=32), '2': Struct(fmt='>f'), '3': String(countType=VarInt(bits=32)), '4': String(countType=VarInt(bits=32)), '5': Container(fields=[{'name': 'blockId', 'type': Struct(fmt='>h')}, {'anon': True, 'type': Switch(fields={'-1': Void()}, compareTo='blockId', default=Container(fields=[{'name': 'itemCount', 'type': Struct(fmt='b')}, {'name': 'itemDamage', 'type': Struct(fmt='>h')}, {'name': 'nbtData', 'type': NBT()}]))}]), '6': Struct(fmt='?'), '7': Container(fields=[{'name': 'pitch', 'type': Struct(fmt='>f')}, {'name': 'yaw', 'type': Struct(fmt='>f')}, {'name': 'roll', 'type': Struct(fmt='>f')}]), '8': BitField(fields=[{'name': 'x', 'size': 26, 'signed': True}, {'name': 'y', 'size': 12, 'signed': True}, {'name': 'z', 'size': 26, 'signed': True}]), '9': Option(type=BitField(fields=[{'name': 'x', 'size': 26, 'signed': True}, {'name': 'y', 'size': 12, 'signed': True}, {'name': 'z', 'size': 26, 'signed': True}])), '10': VarInt(bits=32), '11': Option(type=UUID()), '12': VarInt(bits=32)}, compareTo='type', default=None), endVal=255)}]), 'collect': Container(fields=[{'name': 'collectedEntityId', 'type': VarInt(bits=32)}, {'name': 'collectorEntityId', 'type': VarInt(bits=32)}]), 'spawn_entity': Container(fields=[{'name': 'entityId', 'type': VarInt(bits=32)}, {'name': 'entityUUID', 'type': UUID()}, {'name': 'type', 'type': Struct(fmt='b')}, {'name': 'x', 'type': Struct(fmt='>i')}, {'name': 'y', 'type': Struct(fmt='>i')}, {'name': 'z', 'type': Struct(fmt='>i')}, {'name': 'pitch', 'type': Struct(fmt='b')}, {'name': 'yaw', 'type': Struct(fmt='b')}, {'name': 'objectData', 'type': Struct(fmt='>i')}, {'name': 'velocityX', 'type': Struct(fmt='>h')}, {'name': 'velocityY', 'type': Struct(fmt='>h')}, {'name': 'velocityZ', 'type': Struct(fmt='>h')}]), 'spawn_entity_living': Container(fields=[{'name': 'entityId', 'type': VarInt(bits=32)}, {'name': 'entityUUID', 'type': UUID()}, {'name': 'type', 'type': Struct(fmt='B')}, {'name': 'x', 'type': Struct(fmt='>i')}, {'name': 'y', 'type': Struct(fmt='>i')}, {'name': 'z', 'type': Struct(fmt='>i')}, {'name': 'yaw', 'type': Struct(fmt='b')}, {'name': 'pitch', 'type': Struct(fmt='b')}, {'name': 'headPitch', 'type': Struct(fmt='b')}, {'name': 'velocityX', 'type': Struct(fmt='>h')}, {'name': 'velocityY', 'type': Struct(fmt='>h')}, {'name': 'velocityZ', 'type': Struct(fmt='>h')}, {'name': 'metadata', 'type': EntityMetadataArray(type=Switch(fields={'0': Struct(fmt='b'), '1': VarInt(bits=32), '2': Struct(fmt='>f'), '3': String(countType=VarInt(bits=32)), '4': String(countType=VarInt(bits=32)), '5': Container(fields=[{'name': 'blockId', 'type': Struct(fmt='>h')}, {'anon': True, 'type': Switch(fields={'-1': Void()}, compareTo='blockId', default=Container(fields=[{'name': 'itemCount', 'type': Struct(fmt='b')}, {'name': 'itemDamage', 'type': Struct(fmt='>h')}, {'name': 'nbtData', 'type': NBT()}]))}]), '6': Struct(fmt='?'), '7': Container(fields=[{'name': 'pitch', 'type': Struct(fmt='>f')}, {'name': 'yaw', 'type': Struct(fmt='>f')}, {'name': 'roll', 'type': Struct(fmt='>f')}]), '8': BitField(fields=[{'name': 'x', 'size': 26, 'signed': True}, {'name': 'y', 'size': 12, 'signed': True}, {'name': 'z', 'size': 26, 'signed': True}]), '9': Option(type=BitField(fields=[{'name': 'x', 'size': 26, 'signed': True}, {'name': 'y', 'size': 12, 'signed': True}, {'name': 'z', 'size': 26, 'signed': True}])), '10': VarInt(bits=32), '11': Option(type=UUID()), '12': VarInt(bits=32)}, compareTo='type', default=None), endVal=255)}]), 'spawn_entity_painting': Container(fields=[{'name': 'entityId', 'type': VarInt(bits=32)}, {'name': 'title', 'type': String(countType=VarInt(bits=32))}, {'name': 'location', 'type': BitField(fields=[{'name': 'x', 'size': 26, 'signed': True}, {'name': 'y', 'size': 12, 'signed': True}, {'name': 'z', 'size': 26, 'signed': True}])}, {'name': 'direction', 'type': Struct(fmt='B')}]), 'spawn_entity_experience_orb': Container(fields=[{'name': 'entityId', 'type': VarInt(bits=32)}, {'name': 'x', 'type': Struct(fmt='>i')}, {'name': 'y', 'type': Struct(fmt='>i')}, {'name': 'z', 'type': Struct(fmt='>i')}, {'name': 'count', 'type': Struct(fmt='>h')}]), 'entity_velocity': Container(fields=[{'name': 'entityId', 'type': VarInt(bits=32)}, {'name': 'velocityX', 'type': Struct(fmt='>h')}, {'name': 'velocityY', 'type': Struct(fmt='>h')}, {'name': 'velocityZ', 'type': Struct(fmt='>h')}]), 'entity_destroy': Container(fields=[{'name': 'entityIds', 'type': Array(type=VarInt(bits=32), count=None, countType=VarInt(bits=32))}]), 'entity': Container(fields=[{'name': 'entityId', 'type': VarInt(bits=32)}]), 'rel_entity_move': Container(fields=[{'name': 'entityId', 'type': VarInt(bits=32)}, {'name': 'dX', 'type': Struct(fmt='b')}, {'name': 'dY', 'type': Struct(fmt='b')}, {'name': 'dZ', 'type': Struct(fmt='b')}, {'name': 'onGround', 'type': Struct(fmt='?')}]), 'entity_look': Container(fields=[{'name': 'entityId', 'type': VarInt(bits=32)}, {'name': 'yaw', 'type': Struct(fmt='b')}, {'name': 'pitch', 'type': Struct(fmt='b')}, {'name': 'onGround', 'type': Struct(fmt='?')}]), 'entity_move_look': Container(fields=[{'name': 'entityId', 'type': VarInt(bits=32)}, {'name': 'dX', 'type': Struct(fmt='b')}, {'name': 'dY', 'type': Struct(fmt='b')}, {'name': 'dZ', 'type': Struct(fmt='b')}, {'name': 'yaw', 'type': Struct(fmt='b')}, {'name': 'pitch', 'type': Struct(fmt='b')}, {'name': 'onGround', 'type': Struct(fmt='?')}]), 'entity_teleport': Container(fields=[{'name': 'entityId', 'type': VarInt(bits=32)}, {'name': 'x', 'type': Struct(fmt='>i')}, {'name': 'y', 'type': Struct(fmt='>i')}, {'name': 'z', 'type': Struct(fmt='>i')}, {'name': 'yaw', 'type': Struct(fmt='b')}, {'name': 'pitch', 'type': Struct(fmt='b')}, {'name': 'onGround', 'type': Struct(fmt='?')}]), 'entity_head_rotation': Container(fields=[{'name': 'entityId', 'type': VarInt(bits=32)}, {'name': 'headYaw', 'type': Struct(fmt='b')}]), 'entity_status': Container(fields=[{'name': 'entityId', 'type': Struct(fmt='>i')}, {'name': 'entityStatus', 'type': Struct(fmt='b')}]), 'attach_entity': Container(fields=[{'name': 'entityId', 'type': Struct(fmt='>i')}, {'name': 'vehicleId', 'type': Struct(fmt='>i')}, {'name': 'leash', 'type': Struct(fmt='?')}]), 'entity_metadata': Container(fields=[{'name': 'entityId', 'type': VarInt(bits=32)}, {'name': 'metadata', 'type': EntityMetadataArray(type=Switch(fields={'0': Struct(fmt='b'), '1': VarInt(bits=32), '2': Struct(fmt='>f'), '3': String(countType=VarInt(bits=32)), '4': String(countType=VarInt(bits=32)), '5': Container(fields=[{'name': 'blockId', 'type': Struct(fmt='>h')}, {'anon': True, 'type': Switch(fields={'-1': Void()}, compareTo='blockId', default=Container(fields=[{'name': 'itemCount', 'type': Struct(fmt='b')}, {'name': 'itemDamage', 'type': Struct(fmt='>h')}, {'name': 'nbtData', 'type': NBT()}]))}]), '6': Struct(fmt='?'), '7': Container(fields=[{'name': 'pitch', 'type': Struct(fmt='>f')}, {'name': 'yaw', 'type': Struct(fmt='>f')}, {'name': 'roll', 'type': Struct(fmt='>f')}]), '8': BitField(fields=[{'name': 'x', 'size': 26, 'signed': True}, {'name': 'y', 'size': 12, 'signed': True}, {'name': 'z', 'size': 26, 'signed': True}]), '9': Option(type=BitField(fields=[{'name': 'x', 'size': 26, 'signed': True}, {'name': 'y', 'size': 12, 'signed': True}, {'name': 'z', 'size': 26, 'signed': True}])), '10': VarInt(bits=32), '11': Option(type=UUID()), '12': VarInt(bits=32)}, compareTo='type', default=None), endVal=255)}]), 'entity_effect': Container(fields=[{'name': 'entityId', 'type': VarInt(bits=32)}, {'name': 'effectId', 'type': Struct(fmt='b')}, {'name': 'amplifier', 'type': Struct(fmt='b')}, {'name': 'duration', 'type': VarInt(bits=32)}, {'name': 'hideParticles', 'type': Struct(fmt='?')}]), 'remove_entity_effect': Container(fields=[{'name': 'entityId', 'type': VarInt(bits=32)}, {'name': 'effectId', 'type': Struct(fmt='b')}]), 'experience': Container(fields=[{'name': 'experienceBar', 'type': Struct(fmt='>f')}, {'name': 'level', 'type': VarInt(bits=32)}, {'name': 'totalExperience', 'type': VarInt(bits=32)}]), 'update_attributes': Container(fields=[{'name': 'entityId', 'type': VarInt(bits=32)}, {'name': 'properties', 'type': Array(type=Container(fields=[{'name': 'key', 'type': String(countType=VarInt(bits=32))}, {'name': 'value', 'type': Struct(fmt='>d')}, {'name': 'modifiers', 'type': Array(type=Container(fields=[{'name': 'UUID', 'type': UUID()}, {'name': 'amount', 'type': Struct(fmt='>d')}, {'name': 'operation', 'type': Struct(fmt='b')}]), count=None, countType=VarInt(bits=32))}]), count=None, countType=Struct(fmt='>i'))}]), 'map_chunk': Container(fields=[{'name': 'x', 'type': Struct(fmt='>i')}, {'name': 'z', 'type': Struct(fmt='>i')}, {'name': 'groundUp', 'type': Struct(fmt='?')}, {'name': 'bitMap', 'type': VarInt(bits=32)}, {'name': 'chunkData', 'type': ByteArray(count=None, countType=VarInt(bits=32))}]), 'multi_block_change': Container(fields=[{'name': 'chunkX', 'type': Struct(fmt='>i')}, {'name': 'chunkZ', 'type': Struct(fmt='>i')}, {'name': 'records', 'type': Array(type=Container(fields=[{'name': 'horizontalPos', 'type': Struct(fmt='B')}, {'name': 'y', 'type': Struct(fmt='B')}, {'name': 'blockId', 'type': VarInt(bits=32)}]), count=None, countType=VarInt(bits=32))}]), 'block_change': Container(fields=[{'name': 'location', 'type': BitField(fields=[{'name': 'x', 'size': 26, 'signed': True}, {'name': 'y', 'size': 12, 'signed': True}, {'name': 'z', 'size': 26, 'signed': True}])}, {'name': 'type', 'type': VarInt(bits=32)}]), 'block_action': Container(fields=[{'name': 'location', 'type': BitField(fields=[{'name': 'x', 'size': 26, 'signed': True}, {'name': 'y', 'size': 12, 'signed': True}, {'name': 'z', 'size': 26, 'signed': True}])}, {'name': 'byte1', 'type': Struct(fmt='B')}, {'name': 'byte2', 'type': Struct(fmt='B')}, {'name': 'blockId', 'type': VarInt(bits=32)}]), 'block_break_animation': Container(fields=[{'name': 'entityId', 'type': VarInt(bits=32)}, {'name': 'location', 'type': BitField(fields=[{'name': 'x', 'size': 26, 'signed': True}, {'name': 'y', 'size': 12, 'signed': True}, {'name': 'z', 'size': 26, 'signed': True}])}, {'name': 'destroyStage', 'type': Struct(fmt='b')}]), 'explosion': Container(fields=[{'name': 'x', 'type': Struct(fmt='>f')}, {'name': 'y', 'type': Struct(fmt='>f')}, {'name': 'z', 'type': Struct(fmt='>f')}, {'name': 'radius', 'type': Struct(fmt='>f')}, {'name': 'affectedBlockOffsets', 'type': Array(type=Container(fields=[{'name': 'x', 'type': Struct(fmt='b')}, {'name': 'y', 'type': Struct(fmt='b')}, {'name': 'z', 'type': Struct(fmt='b')}]), count=None, countType=Struct(fmt='>i'))}, {'name': 'playerMotionX', 'type': Struct(fmt='>f')}, {'name': 'playerMotionY', 'type': Struct(fmt='>f')}, {'name': 'playerMotionZ', 'type': Struct(fmt='>f')}]), 'world_event': Container(fields=[{'name': 'effectId', 'type': Struct(fmt='>i')}, {'name': 'location', 'type': BitField(fields=[{'name': 'x', 'size': 26, 'signed': True}, {'name': 'y', 'size': 12, 'signed': True}, {'name': 'z', 'size': 26, 'signed': True}])}, {'name': 'data', 'type': Struct(fmt='>i')}, {'name': 'global', 'type': Struct(fmt='?')}]), 'named_sound_effect': Container(fields=[{'name': 'soundName', 'type': String(countType=VarInt(bits=32))}, {'name': 'x', 'type': Struct(fmt='>i')}, {'name': 'y', 'type': Struct(fmt='>i')}, {'name': 'z', 'type': Struct(fmt='>i')}, {'name': 'volume', 'type': Struct(fmt='>f')}, {'name': 'pitch', 'type': Struct(fmt='B')}]), 'world_particles': Container(fields=[{'name': 'particleId', 'type': Struct(fmt='>i')}, {'name': 'longDistance', 'type': Struct(fmt='?')}, {'name': 'x', 'type': Struct(fmt='>f')}, {'name': 'y', 'type': Struct(fmt='>f')}, {'name': 'z', 'type': Struct(fmt='>f')}, {'name': 'offsetX', 'type': Struct(fmt='>f')}, {'name': 'offsetY', 'type': Struct(fmt='>f')}, {'name': 'offsetZ', 'type': Struct(fmt='>f')}, {'name': 'particleData', 'type': Struct(fmt='>f')}, {'name': 'particles', 'type': Struct(fmt='>i')}, {'name': 'data', 'type': Switch(fields={'36': Array(type=VarInt(bits=32), count=2, countType=None), '37': Array(type=VarInt(bits=32), count=1, countType=None), '38': Array(type=VarInt(bits=32), count=1, countType=None)}, compareTo='particleId', default=Void())}]), 'game_state_change': Container(fields=[{'name': 'reason', 'type': Struct(fmt='B')}, {'name': 'gameMode', 'type': Struct(fmt='>f')}]), 'spawn_entity_weather': Container(fields=[{'name': 'entityId', 'type': VarInt(bits=32)}, {'name': 'type', 'type': Struct(fmt='b')}, {'name': 'x', 'type': Struct(fmt='>i')}, {'name': 'y', 'type': Struct(fmt='>i')}, {'name': 'z', 'type': Struct(fmt='>i')}]), 'open_window': Container(fields=[{'name': 'windowId', 'type': Struct(fmt='B')}, {'name': 'inventoryType', 'type': String(countType=VarInt(bits=32))}, {'name': 'windowTitle', 'type': String(countType=VarInt(bits=32))}, {'name': 'slotCount', 'type': Struct(fmt='B')}, {'name': 'entityId', 'type': Switch(fields={'EntityHorse': Struct(fmt='>i')}, compareTo='inventoryType', default=Void())}]), 'close_window': Container(fields=[{'name': 'windowId', 'type': Struct(fmt='B')}]), 'set_slot': Container(fields=[{'name': 'windowId', 'type': Struct(fmt='b')}, {'name': 'slot', 'type': Struct(fmt='>h')}, {'name': 'item', 'type': Container(fields=[{'name': 'blockId', 'type': Struct(fmt='>h')}, {'anon': True, 'type': Switch(fields={'-1': Void()}, compareTo='blockId', default=Container(fields=[{'name': 'itemCount', 'type': Struct(fmt='b')}, {'name': 'itemDamage', 'type': Struct(fmt='>h')}, {'name': 'nbtData', 'type': NBT()}]))}])}]), 'window_items': Container(fields=[{'name': 'windowId', 'type': Struct(fmt='B')}, {'name': 'items', 'type': Array(type=Container(fields=[{'name': 'blockId', 'type': Struct(fmt='>h')}, {'anon': True, 'type': Switch(fields={'-1': Void()}, compareTo='blockId', default=Container(fields=[{'name': 'itemCount', 'type': Struct(fmt='b')}, {'name': 'itemDamage', 'type': Struct(fmt='>h')}, {'name': 'nbtData', 'type': NBT()}]))}]), count=None, countType=Struct(fmt='>h'))}]), 'craft_progress_bar': Container(fields=[{'name': 'windowId', 'type': Struct(fmt='B')}, {'name': 'property', 'type': Struct(fmt='>h')}, {'name': 'value', 'type': Struct(fmt='>h')}]), 'transaction': Container(fields=[{'name': 'windowId', 'type': Struct(fmt='b')}, {'name': 'action', 'type': Struct(fmt='>h')}, {'name': 'accepted', 'type': Struct(fmt='?')}]), 'update_sign': Container(fields=[{'name': 'location', 'type': BitField(fields=[{'name': 'x', 'size': 26, 'signed': True}, {'name': 'y', 'size': 12, 'signed': True}, {'name': 'z', 'size': 26, 'signed': True}])}, {'name': 'text1', 'type': String(countType=VarInt(bits=32))}, {'name': 'text2', 'type': String(countType=VarInt(bits=32))}, {'name': 'text3', 'type': String(countType=VarInt(bits=32))}, {'name': 'text4', 'type': String(countType=VarInt(bits=32))}]), 'map': Container(fields=[{'name': 'itemDamage', 'type': VarInt(bits=32)}, {'name': 'scale', 'type': Struct(fmt='b')}, {'name': 'trackingPosition', 'type': Struct(fmt='?')}, {'name': 'icons', 'type': Array(type=Container(fields=[{'name': 'directionAndType', 'type': Struct(fmt='b')}, {'name': 'x', 'type': Struct(fmt='b')}, {'name': 'y', 'type': Struct(fmt='b')}]), count=None, countType=VarInt(bits=32))}, {'name': 'columns', 'type': Struct(fmt='b')}, {'name': 'rows', 'type': Switch(fields={'0': Void()}, compareTo='columns', default=Struct(fmt='b'))}, {'name': 'x', 'type': Switch(fields={'0': Void()}, compareTo='columns', default=Struct(fmt='b'))}, {'name': 'y', 'type': Switch(fields={'0': Void()}, compareTo='columns', default=Struct(fmt='b'))}, {'name': 'data', 'type': Switch(fields={'0': Void()}, compareTo='columns', default=ByteArray(count=None, countType=VarInt(bits=32)))}]), 'tile_entity_data': Container(fields=[{'name': 'location', 'type': BitField(fields=[{'name': 'x', 'size': 26, 'signed': True}, {'name': 'y', 'size': 12, 'signed': True}, {'name': 'z', 'size': 26, 'signed': True}])}, {'name': 'action', 'type': Struct(fmt='B')}, {'name': 'nbtData', 'type': NBT()}]), 'open_sign_entity': Container(fields=[{'name': 'location', 'type': BitField(fields=[{'name': 'x', 'size': 26, 'signed': True}, {'name': 'y', 'size': 12, 'signed': True}, {'name': 'z', 'size': 26, 'signed': True}])}]), 'statistics': Container(fields=[{'name': 'entries', 'type': Array(type=Container(fields=[{'name': 'name', 'type': String(countType=VarInt(bits=32))}, {'name': 'value', 'type': VarInt(bits=32)}]), count=None, countType=VarInt(bits=32))}]), 'player_info': Container(fields=[{'name': 'action', 'type': VarInt(bits=32)}, {'name': 'data', 'type': Array(type=Container(fields=[{'name': 'UUID', 'type': UUID()}, {'name': 'name', 'type': Switch(fields={'0': String(countType=VarInt(bits=32))}, compareTo='../action', default=Void())}, {'name': 'properties', 'type': Switch(fields={'0': Array(type=Container(fields=[{'name': 'name', 'type': String(countType=VarInt(bits=32))}, {'name': 'value', 'type': String(countType=VarInt(bits=32))}, {'name': 'signature', 'type': Option(type=String(countType=VarInt(bits=32)))}]), count=None, countType=VarInt(bits=32))}, compareTo='../action', default=Void())}, {'name': 'gamemode', 'type': Switch(fields={'0': VarInt(bits=32), '1': VarInt(bits=32)}, compareTo='../action', default=Void())}, {'name': 'ping', 'type': Switch(fields={'0': VarInt(bits=32), '2': VarInt(bits=32)}, compareTo='../action', default=Void())}, {'name': 'displayName', 'type': Switch(fields={'0': Option(type=String(countType=VarInt(bits=32))), '3': Option(type=String(countType=VarInt(bits=32)))}, compareTo='../action', default=Void())}]), count=None, countType=VarInt(bits=32))}]), 'abilities': Container(fields=[{'name': 'flags', 'type': Struct(fmt='b')}, {'name': 'flyingSpeed', 'type': Struct(fmt='>f')}, {'name': 'walkingSpeed', 'type': Struct(fmt='>f')}]), 'tab_complete': Container(fields=[{'name': 'matches', 'type': Array(type=String(countType=VarInt(bits=32)), count=None, countType=VarInt(bits=32))}]), 'scoreboard_objective': Container(fields=[{'name': 'name', 'type': String(countType=VarInt(bits=32))}, {'name': 'action', 'type': Struct(fmt='b')}, {'name': 'displayText', 'type': Switch(fields={'0': String(countType=VarInt(bits=32)), '2': String(countType=VarInt(bits=32))}, compareTo='action', default=Void())}, {'name': 'type', 'type': Switch(fields={'0': String(countType=VarInt(bits=32)), '2': String(countType=VarInt(bits=32))}, compareTo='action', default=Void())}]), 'scoreboard_score': Container(fields=[{'name': 'itemName', 'type': String(countType=VarInt(bits=32))}, {'name': 'action', 'type': Struct(fmt='b')}, {'name': 'scoreName', 'type': String(countType=VarInt(bits=32))}, {'name': 'value', 'type': Switch(fields={'1': Void()}, compareTo='action', default=VarInt(bits=32))}]), 'scoreboard_display_objective': Container(fields=[{'name': 'position', 'type': Struct(fmt='b')}, {'name': 'name', 'type': String(countType=VarInt(bits=32))}]), 'scoreboard_team': Container(fields=[{'name': 'team', 'type': String(countType=VarInt(bits=32))}, {'name': 'mode', 'type': Struct(fmt='b')}, {'name': 'name', 'type': Switch(fields={'0': String(countType=VarInt(bits=32)), '2': String(countType=VarInt(bits=32))}, compareTo='mode', default=Void())}, {'name': 'prefix', 'type': Switch(fields={'0': String(countType=VarInt(bits=32)), '2': String(countType=VarInt(bits=32))}, compareTo='mode', default=Void())}, {'name': 'suffix', 'type': Switch(fields={'0': String(countType=VarInt(bits=32)), '2': String(countType=VarInt(bits=32))}, compareTo='mode', default=Void())}, {'name': 'friendlyFire', 'type': Switch(fields={'0': Struct(fmt='b'), '2': Struct(fmt='b')}, compareTo='mode', default=Void())}, {'name': 'nameTagVisibility', 'type': Switch(fields={'0': String(countType=VarInt(bits=32)), '2': String(countType=VarInt(bits=32))}, compareTo='mode', default=Void())}, {'name': 'collisionRule', 'type': Switch(fields={'0': String(countType=VarInt(bits=32)), '2': String(countType=VarInt(bits=32))}, compareTo='mode', default=Void())}, {'name': 'color', 'type': Switch(fields={'0': Struct(fmt='b'), '2': Struct(fmt='b')}, compareTo='mode', default=Void())}, {'name': 'players', 'type': Switch(fields={'0': Array(type=String(countType=VarInt(bits=32)), count=None, countType=VarInt(bits=32)), '3': Array(type=String(countType=VarInt(bits=32)), count=None, countType=VarInt(bits=32)), '4': Array(type=String(countType=VarInt(bits=32)), count=None, countType=VarInt(bits=32))}, compareTo='mode', default=Void())}]), 'custom_payload': Container(fields=[{'name': 'channel', 'type': String(countType=VarInt(bits=32))}, {'name': 'data', 'type': ByteArray(count=None, countType=None)}]), 'kick_disconnect': Container(fields=[{'name': 'reason', 'type': String(countType=VarInt(bits=32))}]), 'difficulty': Container(fields=[{'name': 'difficulty', 'type': Struct(fmt='B')}]), 'combat_event': Container(fields=[{'name': 'event', 'type': VarInt(bits=32)}, {'name': 'duration', 'type': Switch(fields={'1': VarInt(bits=32)}, compareTo='event', default=Void())}, {'name': 'playerId', 'type': Switch(fields={'2': VarInt(bits=32)}, compareTo='event', default=Void())}, {'name': 'entityId', 'type': Switch(fields={'1': Struct(fmt='>i'), '2': Struct(fmt='>i')}, compareTo='event', default=Void())}, {'name': 'message', 'type': Switch(fields={'2': String(countType=VarInt(bits=32))}, compareTo='event', default=Void())}]), 'camera': Container(fields=[{'name': 'cameraId', 'type': VarInt(bits=32)}]), 'world_border': Container(fields=[{'name': 'action', 'type': VarInt(bits=32)}, {'name': 'radius', 'type': Switch(fields={'0': Struct(fmt='>d')}, compareTo='action', default=Void())}, {'name': 'x', 'type': Switch(fields={'2': Struct(fmt='>d'), '3': Struct(fmt='>d')}, compareTo='action', default=Void())}, {'name': 'z', 'type': Switch(fields={'2': Struct(fmt='>d'), '3': Struct(fmt='>d')}, compareTo='action', default=Void())}, {'name': 'old_radius', 'type': Switch(fields={'1': Struct(fmt='>d'), '3': Struct(fmt='>d')}, compareTo='action', default=Void())}, {'name': 'new_radius', 'type': Switch(fields={'1': Struct(fmt='>d'), '3': Struct(fmt='>d')}, compareTo='action', default=Void())}, {'name': 'speed', 'type': Switch(fields={'1': VarInt(bits=32), '3': VarInt(bits=32)}, compareTo='action', default=Void())}, {'name': 'portalBoundary', 'type': Switch(fields={'3': VarInt(bits=32)}, compareTo='action', default=Void())}, {'name': 'warning_time', 'type': Switch(fields={'3': VarInt(bits=32), '4': VarInt(bits=32)}, compareTo='action', default=Void())}, {'name': 'warning_blocks', 'type': Switch(fields={'3': VarInt(bits=32), '5': VarInt(bits=32)}, compareTo='action', default=Void())}]), 'title': Container(fields=[{'name': 'action', 'type': VarInt(bits=32)}, {'name': 'text', 'type': Switch(fields={'0': String(countType=VarInt(bits=32)), '1': String(countType=VarInt(bits=32))}, compareTo='action', default=Void())}, {'name': 'fadeIn', 'type': Switch(fields={'2': Struct(fmt='>i')}, compareTo='action', default=Void())}, {'name': 'stay', 'type': Switch(fields={'2': Struct(fmt='>i')}, compareTo='action', default=Void())}, {'name': 'fadeOut', 'type': Switch(fields={'2': Struct(fmt='>i')}, compareTo='action', default=Void())}]), 'set_compression': Container(fields=[{'name': 'threshold', 'type': VarInt(bits=32)}]), 'playerlist_header': Container(fields=[{'name': 'header', 'type': String(countType=VarInt(bits=32))}, {'name': 'footer', 'type': String(countType=VarInt(bits=32))}]), 'resource_pack_send': Container(fields=[{'name': 'url', 'type': String(countType=VarInt(bits=32))}, {'name': 'hash', 'type': String(countType=VarInt(bits=32))}]), 'boss_bar': Container(fields=[{'name': 'entityUUID', 'type': UUID()}, {'name': 'action', 'type': VarInt(bits=32)}, {'name': 'title', 'type': Switch(fields={'0': String(countType=VarInt(bits=32)), '3': String(countType=VarInt(bits=32))}, compareTo='action', default=Void())}, {'name': 'health', 'type': Switch(fields={'0': Struct(fmt='>f'), '2': Struct(fmt='>f')}, compareTo='action', default=Void())}, {'name': 'color', 'type': Switch(fields={'0': VarInt(bits=32), '4': VarInt(bits=32)}, compareTo='action', default=Void())}, {'name': 'dividers', 'type': Switch(fields={'0': VarInt(bits=32), '4': VarInt(bits=32)}, compareTo='action', default=Void())}, {'name': 'flags', 'type': Switch(fields={'0': Struct(fmt='B'), '5': Struct(fmt='B')}, compareTo='action', default=Void())}]), 'set_cooldown': Container(fields=[{'name': 'itemID', 'type': VarInt(bits=32)}, {'name': 'cooldownTicks', 'type': VarInt(bits=32)}]), 'unload_chunk': Container(fields=[{'name': 'chunkX', 'type': Struct(fmt='>i')}, {'name': 'chunkZ', 'type': Struct(fmt='>i')}])}, compareTo='name', default=None)}])
packet_play_up = Container(fields=[{'name': 'name', 'type': Mapper(type=VarInt(bits=32), mappings={'0x0a': 'keep_alive', '0x01': 'chat', '0x09': 'use_entity', '0x0e': 'flying', '0x0b': 'position', '0x0d': 'look', '0x0c': 'position_look', '0x10': 'block_dig', '0x19': 'block_place', '0x14': 'held_item_slot', '0x17': 'arm_animation', '0x11': 'entity_action', '0x12': 'steer_vehicle', '0x07': 'close_window', '0x06': 'window_click', '0x04': 'transaction', '0x15': 'set_creative_slot', '0x05': 'enchant_item', '0x16': 'update_sign', '0x0f': 'abilities', '0x00': 'tab_complete', '0x03': 'settings', '0x02': 'client_command', '0x08': 'custom_payload', '0x18': 'spectate', '0x13': 'resource_pack_receive', '0x1a': 'use_item'})}, {'name': 'params', 'type': Switch(fields={'keep_alive': Container(fields=[{'name': 'keepAliveId', 'type': VarInt(bits=32)}]), 'chat': Container(fields=[{'name': 'message', 'type': String(countType=VarInt(bits=32))}]), 'use_entity': Container(fields=[{'name': 'target', 'type': VarInt(bits=32)}, {'name': 'mouse', 'type': VarInt(bits=32)}, {'name': 'x', 'type': Switch(fields={'2': Struct(fmt='>f')}, compareTo='mouse', default=Void())}, {'name': 'y', 'type': Switch(fields={'2': Struct(fmt='>f')}, compareTo='mouse', default=Void())}, {'name': 'z', 'type': Switch(fields={'2': Struct(fmt='>f')}, compareTo='mouse', default=Void())}, {'name': 'hand', 'type': Switch(fields={'0': VarInt(bits=32), '2': VarInt(bits=32)}, compareTo='mouse', default=Void())}]), 'flying': Container(fields=[{'name': 'onGround', 'type': Struct(fmt='?')}]), 'position': Container(fields=[{'name': 'x', 'type': Struct(fmt='>d')}, {'name': 'y', 'type': Struct(fmt='>d')}, {'name': 'z', 'type': Struct(fmt='>d')}, {'name': 'onGround', 'type': Struct(fmt='?')}]), 'look': Container(fields=[{'name': 'yaw', 'type': Struct(fmt='>f')}, {'name': 'pitch', 'type': Struct(fmt='>f')}, {'name': 'onGround', 'type': Struct(fmt='?')}]), 'position_look': Container(fields=[{'name': 'x', 'type': Struct(fmt='>d')}, {'name': 'y', 'type': Struct(fmt='>d')}, {'name': 'z', 'type': Struct(fmt='>d')}, {'name': 'yaw', 'type': Struct(fmt='>f')}, {'name': 'pitch', 'type': Struct(fmt='>f')}, {'name': 'onGround', 'type': Struct(fmt='?')}]), 'block_dig': Container(fields=[{'name': 'status', 'type': Struct(fmt='b')}, {'name': 'location', 'type': BitField(fields=[{'name': 'x', 'size': 26, 'signed': True}, {'name': 'y', 'size': 12, 'signed': True}, {'name': 'z', 'size': 26, 'signed': True}])}, {'name': 'face', 'type': Struct(fmt='b')}]), 'block_place': Container(fields=[{'name': 'location', 'type': BitField(fields=[{'name': 'x', 'size': 26, 'signed': True}, {'name': 'y', 'size': 12, 'signed': True}, {'name': 'z', 'size': 26, 'signed': True}])}, {'name': 'direction', 'type': VarInt(bits=32)}, {'name': 'hand', 'type': VarInt(bits=32)}, {'name': 'cursorX', 'type': Struct(fmt='b')}, {'name': 'cursorY', 'type': Struct(fmt='b')}, {'name': 'cursorZ', 'type': Struct(fmt='b')}]), 'held_item_slot': Container(fields=[{'name': 'slotId', 'type': Struct(fmt='>h')}]), 'arm_animation': Container(fields=[{'name': 'hand', 'type': VarInt(bits=32)}]), 'entity_action': Container(fields=[{'name': 'entityId', 'type': VarInt(bits=32)}, {'name': 'actionId', 'type': VarInt(bits=32)}, {'name': 'jumpBoost', 'type': VarInt(bits=32)}]), 'steer_vehicle': Container(fields=[{'name': 'sideways', 'type': Struct(fmt='>f')}, {'name': 'forward', 'type': Struct(fmt='>f')}, {'name': 'jump', 'type': Struct(fmt='B')}]), 'close_window': Container(fields=[{'name': 'windowId', 'type': Struct(fmt='B')}]), 'window_click': Container(fields=[{'name': 'windowId', 'type': Struct(fmt='B')}, {'name': 'slot', 'type': Struct(fmt='>h')}, {'name': 'mouseButton', 'type': Struct(fmt='b')}, {'name': 'action', 'type': Struct(fmt='>h')}, {'name': 'mode', 'type': Struct(fmt='b')}, {'name': 'item', 'type': Container(fields=[{'name': 'blockId', 'type': Struct(fmt='>h')}, {'anon': True, 'type': Switch(fields={'-1': Void()}, compareTo='blockId', default=Container(fields=[{'name': 'itemCount', 'type': Struct(fmt='b')}, {'name': 'itemDamage', 'type': Struct(fmt='>h')}, {'name': 'nbtData', 'type': NBT()}]))}])}]), 'transaction': Container(fields=[{'name': 'windowId', 'type': Struct(fmt='b')}, {'name': 'action', 'type': Struct(fmt='>h')}, {'name': 'accepted', 'type': Struct(fmt='?')}]), 'set_creative_slot': Container(fields=[{'name': 'slot', 'type': Struct(fmt='>h')}, {'name': 'item', 'type': Container(fields=[{'name': 'blockId', 'type': Struct(fmt='>h')}, {'anon': True, 'type': Switch(fields={'-1': Void()}, compareTo='blockId', default=Container(fields=[{'name': 'itemCount', 'type': Struct(fmt='b')}, {'name': 'itemDamage', 'type': Struct(fmt='>h')}, {'name': 'nbtData', 'type': NBT()}]))}])}]), 'enchant_item': Container(fields=[{'name': 'windowId', 'type': Struct(fmt='b')}, {'name': 'enchantment', 'type': Struct(fmt='b')}]), 'update_sign': Container(fields=[{'name': 'location', 'type': BitField(fields=[{'name': 'x', 'size': 26, 'signed': True}, {'name': 'y', 'size': 12, 'signed': True}, {'name': 'z', 'size': 26, 'signed': True}])}, {'name': 'text1', 'type': String(countType=VarInt(bits=32))}, {'name': 'text2', 'type': String(countType=VarInt(bits=32))}, {'name': 'text3', 'type': String(countType=VarInt(bits=32))}, {'name': 'text4', 'type': String(countType=VarInt(bits=32))}]), 'abilities': Container(fields=[{'name': 'flags', 'type': Struct(fmt='b')}, {'name': 'flyingSpeed', 'type': Struct(fmt='>f')}, {'name': 'walkingSpeed', 'type': Struct(fmt='>f')}]), 'tab_complete': Container(fields=[{'name': 'text', 'type': String(countType=VarInt(bits=32))}, {'name': 'block', 'type': Option(type=BitField(fields=[{'name': 'x', 'size': 26, 'signed': True}, {'name': 'y', 'size': 12, 'signed': True}, {'name': 'z', 'size': 26, 'signed': True}]))}]), 'settings': Container(fields=[{'name': 'locale', 'type': String(countType=VarInt(bits=32))}, {'name': 'viewDistance', 'type': Struct(fmt='b')}, {'name': 'chatFlags', 'type': VarInt(bits=32)}, {'name': 'chatColors', 'type': Struct(fmt='?')}, {'name': 'skinParts', 'type': Struct(fmt='B')}, {'name': 'mainHand', 'type': VarInt(bits=32)}]), 'client_command': Container(fields=[{'name': 'payload', 'type': VarInt(bits=32)}]), 'custom_payload': Container(fields=[{'name': 'channel', 'type': String(countType=VarInt(bits=32))}, {'name': 'data', 'type': ByteArray(count=None, countType=None)}]), 'spectate': Container(fields=[{'name': 'target', 'type': UUID()}]), 'resource_pack_receive': Container(fields=[{'name': 'hash', 'type': String(countType=VarInt(bits=32))}, {'name': 'result', 'type': VarInt(bits=32)}]), 'use_item': Container(fields=[{'name': 'hand', 'type': VarInt(bits=32)}])}, compareTo='name', default=None)}])