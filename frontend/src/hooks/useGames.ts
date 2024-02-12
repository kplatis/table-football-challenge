import { Game } from '@/types/games'
import axios from 'axios'
import { useQuery } from 'react-query'

export default function useGames() {
  return useQuery({
    queryKey: 'games',
    queryFn: async (): Promise<Game[]> => {
      const { data } = await axios.get('http://localhost:8000/games')
      return data
    },
  })
}
