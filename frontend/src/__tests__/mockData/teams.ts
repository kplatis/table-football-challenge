import { Team } from '@/types/teams'

export const mockTeams: Team[] = [
  {
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
  {
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
]
