import { Team } from '@/types/teams'
import axios from 'axios'
import { useQuery } from 'react-query'

export default function useTeams() {
  return useQuery({
    queryKey: 'teams',
    queryFn: async (): Promise<Team[]> => {
      const { data } = await axios.get('http://localhost:8000/teams')
      return data
    },
  })
}
