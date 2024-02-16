import { Game } from '@/types/games'

export const mockGames: Game[] = [
  {
    first_team_goals: 2,
    second_team_goals: 1,
    id: 1,
    first_team_id: 1,
    second_team_id: 2,
    first_team: {
      name: 'team1',
      id: 1,
      first_player_id: 1,
      second_player_id: 3,
      first_player: {
        name: 'Player1',
        id: 1,
      },
      second_player: {
        name: 'Player3',
        id: 3,
      },
    },
    second_team: {
      name: 'team2',
      id: 2,
      first_player_id: 2,
      second_player_id: 4,
      first_player: {
        name: 'Player2',
        id: 2,
      },
      second_player: {
        name: 'Player4',
        id: 4,
      },
    },
  },
  {
    first_team_goals: 6,
    second_team_goals: 0,
    id: 4,
    first_team_id: 3,
    second_team_id: 4,
    first_team: {
      name: 'team3',
      id: 3,
      first_player_id: 1,
      second_player_id: null,
      first_player: {
        name: 'Player1',
        id: 1,
      },
      second_player: null,
    },
    second_team: {
      name: 'team4',
      id: 4,
      first_player_id: 3,
      second_player_id: null,
      first_player: {
        name: 'Player3',
        id: 3,
      },
      second_player: null,
    },
  },
]
