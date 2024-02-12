import { Player } from '@/types/players'
import axios from 'axios'
import { useQuery } from 'react-query'

export default function usePlayers() {
  return useQuery({
    queryKey: ['posts'],
    queryFn: async (): Promise<Player[]> => {
      const { data } = await axios.get('http://localhost:8000/players')
      return data
    },
  })
}
