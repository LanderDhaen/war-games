# War Games

War Games is a Discord bot for configuring and running structured community tournaments. It keeps
the tournament workflow inside Discord by managing the roles, channels, and commands used by
hosts and participants.

## Commands

| Command                                  | Description                                     | Access        |
| ---------------------------------------- | ----------------------------------------------- | ------------- |
| [`/server configure`](#server-configure) | Update the server configuration for War Games.  | Administrator |
| [`/server info`](#server-info)           | Display the server configuration for War Games. | Administrator |
| [`/server debug`](#server-debug)         | Debug the server configuration for War Games.   | Administrator |

## Server

Manage your server for War Games.

### `/server configure`

![Administrator permission](https://img.shields.io/badge/permission-Administrator-d73a49)

Update the server configuration for War Games.

```text
/server configure host-role: participant-role: game-channel: results-channel:
```

#### Parameters

| Parameter          | Type         | Required | Description                                     |
| ------------------ | ------------ | :------: | ----------------------------------------------- |
| `host-role`        | Role         |   Yes    | The role that will be assigned to hosts.        |
| `participant-role` | Role         |   Yes    | The role that will be assigned to participants. |
| `game-channel`     | Text channel |   Yes    | The channel where games will be posted.         |
| `results-channel`  | Text channel |   Yes    | The channel where game results will be posted.  |

### `/server info`

![Administrator permission](https://img.shields.io/badge/permission-Administrator-d73a49)

Display the server configuration for War Games.

```text
/server info
```

### `/server debug`

![Administrator permission](https://img.shields.io/badge/permission-Administrator-d73a49)

Debug the server configuration for War Games.

```text
/server debug
```
