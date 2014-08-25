$TTL    3600
@       IN      SOA     sid.example.com. root.example.com. (
                   2007010401           ; Serial
                         3600           ; Refresh [1h]
                          600           ; Retry   [10m]
                        86400           ; Expire  [1d]
                          600 )         ; Negative Cache TTL [1h]
;
@       IN      NS      sid.example.com.
@       IN      MX      10 sid.example.com.

sid     IN      A       192.168.0.1
etch    IN      A       192.168.0.2

pop     IN      CNAME   sid
www     IN      CNAME   sid
mail    IN      CNAME   sid
