import json

x='{"end_device_ids":{"device_id":"eui-a81758fffe086f8d","application_ids":{"application_id":"iutbiot51"},"dev_eui":"A81758FFFE086F8D","join_eui":"0000000000000000","dev_addr":"260B957D"},"correlation_ids":["as🆙01GM57V3DJYSTEZDH524913J15","gs:conn:01GM38P73ABVS1NAP0801WCY4A","gs🆙host:01GM38P742B433S3CJTDE27DR5","gs:uplink:01GM57V3719GGCJKEH72AWV8","ns:uplink:01GM57V372AZCFF7H1JCXAY37J","rpc:/ttn.lorawan.v3.GsNs/HandleUplink:01GM57V372RDVWJVQDSR9RGPFF","rpc:/ttn.lorawan.v3.NsAs/HandleUplink:01GM57V3DJ4465E5MAEHZFRATK"],"received_at":"2022-12-13T07:57:58.578449987Z","uplink_message":{"session_key_id":"AYT3XhXhoK9kJRhGRAPn0A==","f_port":5,"f_cnt":5242,"frm_payload":"AQAqAlUEADwFAAcOVQ==","decoded_payload":{"humidity":85,"light":60,"motion":0,"temperature":4.2,"vdd":3669},"rx_metadata":[{"gateway_ids":{"gateway_id":"0080000000025ca1","eui":"0080000000025CA1"},"timestamp":1160172307,"rssi":-104,"channel_rssi":-104,"snr":3,"location":{"latitude":43.346686503459594,"longitude":3.2223054311180026,"source":"SOURCE_REGISTRY"},"uplink_token":"Ch4KHAoQMDA4MDAwMDAwMDAyNWNhMRIIAIAAAAACXKEQk6abqQQaDAiG4eCcBhCC0qywASC4hKL94fEP","channel_index":4,"received_at":"2022-12-13T07:57:58.354517410Z"},{"gateway_ids":{"gateway_id":"lisah-momac-ug65","eui":"24E124FFFEF3D22F"},"time":"2022-12-13T07:57:58.340Z","timestamp":4099092421,"rssi":-114,"channel_rssi":-114,"snr":4.2,"frequency_offset":"-23620","location":{"latitude":43.619471719105505,"longitude":3.8574537634849553,"altitude":80,"source":"SOURCE_REGISTRY"},"uplink_token":"Ch4KHAoQbGlzYWgtbW9tYWMtdWc2NRIIJOEk//7z0i8Qxd/Mog8aDAiG4eCcBhDC48SzASCIs8qnpsoPKgwIhuHgnAYQgPqPogE=","channel_index":4,"gps_time":"2022-12-13T07:57:58.340Z","received_at":"2022-12-13T07:57:58.358417372Z"}],"settings":{"data_rate":{"lora":{"bandwidth":125000,"spreading_factor":7,"coding_rate":"4/5"}},"frequency":"867300000","timestamp":1160172307},"received_at":"2022-12-13T07:57:58.370839657Z","consumed_airtime":"0.061696s","network_ids":{"net_id":"000013","tenant_id":"ttn","cluster_id":"eu1","cluster_address":"eu1.cloud.thethings.network"}}}'

data = json.loads(x)
print(data.get("uplink_message").get('decoded_payload'))