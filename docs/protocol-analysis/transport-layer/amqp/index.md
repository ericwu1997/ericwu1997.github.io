---
title: (TCP 5672:5671) AMQP - Advanced Message Queuing Protocol
parent: Transport Layer
---

# AMQP (Advanced Message Queuing Protocol)
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

### Overview
AMQP (Advanced Message Queuing Protocol) is an open standard for message-oriented communication that enables reliable and interoperable data exchange between distributed systems. It defines a binary protocol for framing, routing, and delivering messages, supporting patterns such as publish/subscribe, request/response, and point-to-point. AMQP ensures features like guaranteed delivery, message acknowledgment, and flexible routing through exchanges and queues, and is widely used in enterprise integration and cloud services.

### General Frame Format
```
0      1         3         7                size+7     size+8
+------+---------+---------+ +-------------+ +-----------+
| type | channel | size    | |   payload   | | frame-end |
+------+---------+---------+ +-------------+ +-----------+
 octet   short     long        'size' octets     octet
```
```
AMQP defines these frame types:
* Type = 1, "METHOD": method frame.
* Type = 2, "HEADER": content header frame.
* Type = 3, "BODY": content body frame.
* Type = 4, "HEARTBEAT": heartbeat frame.
```

### Method Payloads
```
0          2           4
+----------+-----------+-------------- - -
| class-id | method-id | arguments...
+----------+-----------+-------------- - -
    short      short   ...
```

### Property and Method Summary

| **Class**     | **ID** | **Short Class Description**         | **Method**      | **ID** | **Short Method Description**                      |
|----------------|--------|------------------------------------|-----------------|--------|---------------------------------------------------|
| connection     | 10     | work with socket connections       | start           | 10     | start connection negotiation                      |
|                |        |                                    | start-ok        | 11     | select security mechanism and locale              |
|                |        |                                    | secure          | 20     | security mechanism challenge                      |
|                |        |                                    | secure-ok       | 21     | security mechanism response                       |
|                |        |                                    | tune            | 30     | propose connection tuning parameters              |
|                |        |                                    | tune-ok         | 31     | negotiate connection tuning parameters            |
|                |        |                                    | open            | 40     | open connection to virtual host                   |
|                |        |                                    | open-ok         | 41     | signal that connection is ready                   |
|                |        |                                    | close           | 50     | request a connection close                        |
|                |        |                                    | close-ok        | 51     | confirm a connection close                        |
| channel        | 20     | work with channels                 | open            | 10     | open a channel for use                            |
|                |        |                                    | open-ok         | 11     | signal that the channel is ready                  |
|                |        |                                    | flow            | 20     | enable/disable flow from peer                     |
|                |        |                                    | flow-ok         | 21     | confirm a flow method                             |
|                |        |                                    | close           | 40     | request a channel close                           |
|                |        |                                    | close-ok        | 41     | confirm a channel close                           |
| exchange       | 40     | work with exchanges                | declare         | 10     | verify exchange exists, create if needed          |
|                |        |                                    | declare-ok      | 11     | confirm exchange declaration                      |
|                |        |                                    | delete          | 20     | delete an exchange                                |
|                |        |                                    | delete-ok       | 21     | confirm deletion of an exchange                   |
| queue          | 50     | work with queues                   | declare         | 10     | declare queue, create if needed                   |
|                |        |                                    | declare-ok      | 11     | confirms a queue definition                       |
|                |        |                                    | bind            | 20     | bind queue to an exchange                         |
|                |        |                                    | bind-ok         | 21     | confirm bind successful                           |
|                |        |                                    | purge           | 30     | purge a queue                                     |
|                |        |                                    | purge-ok        | 31     | confirms a queue purge                            |
|                |        |                                    | delete          | 40     | delete a queue                                    |
|                |        |                                    | delete-ok       | 41     | confirm deletion of a queue                       |
|                |        |                                    | unbind          | 50     | unbind a queue from an exchange                   |
|                |        |                                    | unbind-ok       | 51     | confirm unbind successful                         |
| basic          | 60     | work with basic content            | qos             | 10     | specify quality of service                        |
|                |        |                                    | qos-ok          | 11     | confirm the requested qos                         |
|                |        |                                    | consume         | 20     | start a queue consumer                            |
|                |        |                                    | consume-ok      | 21     | confirm a new consumer                            |
|                |        |                                    | cancel          | 30     | end a queue consumer                              |
|                |        |                                    | cancel-ok       | 31     | confirm a cancelled consumer                      |
|                |        |                                    | publish         | 40     | publish a message                                 |
|                |        |                                    | return          | 50     | return a failed message                           |
|                |        |                                    | deliver         | 60     | notify the client of a consumer message           |
|                |        |                                    | get             | 70     | direct access to a queue                          |
|                |        |                                    | get-ok          | 71     | provide client with a message                     |
|                |        |                                    | get-empty       | 72     | indicate no messages available                    |
|                |        |                                    | ack             | 80     | acknowledge one or more messages                  |
|                |        |                                    | reject          | 90     | reject an incoming message                        |
|                |        |                                    | recover-async   | 100    | redeliver unacknowledged messages                 |
|                |        |                                    | recover         | 110    | redeliver unacknowledged messages                 |
|                |        |                                    | recover-ok      | 111    | confirm recovery                                  |
| tx             | 90     | work with transactions             | select          | 10     | select standard transaction mode                  |
|                |        |                                    | select-ok       | 11     | confirm transaction mode                          |
|                |        |                                    | commit          | 20     | commit the current transaction                    |
|                |        |                                    | commit-ok       | 21     | confirm a successful commit                       |
|                |        |                                    | rollback        | 30     | abandon the current transaction                   |
|                |        |                                    | rollback-ok     | 31     | confirm successful rollback                       |

### Sample Hexdump
Protocol Header. The client MUST start a new connection by sending a protocol header. This is an 8-octet sequence:
```
Advanced Message Queuing Protocol
    Type: Method (1)
    Channel: 0
    Length: 524
    Class: Connection (10)
    Method: Start (10)
    Arguments

0000   41 4d 51 50 00 00 09 01                           AMQP....
```

Connection.Open
```
Advanced Message Queuing Protocol
    Type: Method (1)
    Channel: 0
    Length: 8
    Class: Connection (10)
    Method: Open (40)
    Arguments
        Virtual-Host: /
        Capabilities: 
        .... ...1 = Insist: True

0000   01 00 00 00 00 00 08 00 0a 00 28 01 2f 00 01 ce   ..........(./...
```



### Reference
[https://github.com/ericwu1997/references/blob/master/amqp-specification.zip](amqp-specification.zip)<br>