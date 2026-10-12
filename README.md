# War Games

War Games is a Discord bot for configuring and running structured community tournaments. It keeps
the tournament workflow inside Discord by managing the roles, channels, and commands used by
hosts and participants.

## Commands

| Command                                        | Description                                        | Access        |
| ---------------------------------------------- | -------------------------------------------------- | ------------- |
| [`/server configure`](#server-configure)       | Update the server configuration for War Games.     | Administrator |
| [`/server info`](#server-info)                 | Display the server configuration for War Games.    | Administrator |
| [`/server debug`](#server-debug)               | Debug the server configuration for War Games.      | Administrator |
| [`/tournament schedule`](#tournament-schedule) | Schedule a new War Games tournament.               | Host role     |
| [`/tournament info`](#tournament-info)         | Display the information for a War Games tournament | Everyone      |
| [`/tournament list`](#tournament-list)         | Display a list of War Games tournaments            | Everyone      |
| [`/tournament start`](#tournament-start)       | Start a scheduled War Games tournament             | Host role     |
| [`/tournament end`](#tournament-end)           | End an active War Games tournament                 | Host role     |

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

## Tournament

Manage your War Games tournaments.

### `/tournament schedule`

![Host role required](https://img.shields.io/badge/permission-Host%20role-e99613)

Schedule a new War Games tournament. Tournament names must be unique within the server.

```text
/tournament schedule name: team-size: description:
```

#### Parameters

| Parameter     | Type                    | Required | Description                              |
| ------------- | ----------------------- | :------: | ---------------------------------------- |
| `name`        | Text (1–50 characters)  |   Yes    | The name of the tournament.              |
| `team-size`   | Integer (1–50)          |   Yes    | The size of each team in the tournament. |
| `description` | Text (1–512 characters) |    No    | The description of the tournament.       |

### `/tournament info`

![Available to everyone](https://img.shields.io/badge/permission-Everyone-2da44e)

Display the information for a War Games tournament

```text
/tournament info tournament:
```

#### Parameters

| Parameter    | Type                      | Required | Description                 |
| ------------ | ------------------------- | :------: | --------------------------- |
| `tournament` | Tournament (autocomplete) |   Yes    | The name of the tournament. |

### `/tournament list`

![Available to everyone](https://img.shields.io/badge/permission-Everyone-2da44e)

Display a list of War Games tournaments

```text
/tournament list status:
```

#### Parameters

| Parameter | Type                                 | Required | Description                            |
| --------- | ------------------------------------ | :------: | -------------------------------------- |
| `status`  | `Scheduled`, `Active`, or `Finished` |   Yes    | The status of the tournaments to list. |

### `/tournament start`

![Host role required](https://img.shields.io/badge/permission-Host%20role-e99613)

Start a scheduled War Games tournament

```text
/tournament start tournament:
```

#### Parameters

| Parameter    | Type                                | Required | Description                 |
| ------------ | ----------------------------------- | :------: | --------------------------- |
| `tournament` | Scheduled tournament (autocomplete) |   Yes    | The name of the tournament. |

### `/tournament end`

![Host role required](https://img.shields.io/badge/permission-Host%20role-e99613)

End an active War Games tournament

```text
/tournament end tournament:
```

#### Parameters

| Parameter    | Type                             | Required | Description                 |
| ------------ | -------------------------------- | :------: | --------------------------- |
| `tournament` | Active tournament (autocomplete) |   Yes    | The name of the tournament. |
