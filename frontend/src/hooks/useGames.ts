import { Game } from '@/types/games'
import axios from 'axios'
import { useQuery } from 'react-query'

export default function useGames(firstTeamId?: number, secondTeamId?: number) {
  return useQuery({
    queryKey: ['games', firstTeamId, secondTeamId],
    queryFn: async (): Promise<Game[]> => {
      let url = 'http://localhost:8000/games'
      if (firstTeamId && secondTeamId) {
        url = `http://localhost:8000/games?versus_team_ids=${firstTeamId}&versus_team_ids=${secondTeamId}`
      }

      const { data } = await axios.get(url)
      return data
    },
  })
}
