'use client'

import { Team } from '@/types/teams'
import TeamSelectionForm from '../TeamSelectionForm'
import { useState } from 'react'
import useTeams from '@/hooks/useTeams'
import { Center, Loader } from '@mantine/core'
import StatisticsScore from '@/components/statistics/StatisticsScore'

type TeamSelectioState = {
  firstTeam?: Team
  secondTeam?: Team
}

export default function TeamComparison() {
  const { isLoading, data } = useTeams()
  const [selectedTeams, setSelectedTeams] = useState<TeamSelectioState>({
    firstTeam: undefined,
    secondTeam: undefined,
  })

  const setSelected = (firstTeamId: number, secondTeamId: number) => {
    const firstTeam = data?.find((team) => team.id === firstTeamId)
    const secondTeam = data?.find((team) => team.id === secondTeamId)

    setSelectedTeams({
      firstTeam: firstTeam,
      secondTeam: secondTeam,
    })
  }

  if (isLoading) {
    return (
      <Center>
        <Loader color="blue" />
      </Center>
    )
  }
  if (data) {
    return (
      <>
        <TeamSelectionForm
          teams={data}
          submissionButtonText="Compare!"
          setTeamsFn={setSelected}
        />
        {selectedTeams.firstTeam && selectedTeams.secondTeam && (
          <StatisticsScore
            firstTeam={selectedTeams.firstTeam}
            secondTeam={selectedTeams.secondTeam}
          />
        )}
      </>
    )
  }
}
