'use client'

import {
  Button,
  Center,
  Group,
  Loader,
  NumberInput,
  Select,
  SimpleGrid,
} from '@mantine/core'
import { notifications } from '@mantine/notifications'
import { useForm } from '@mantine/form'
import axios from 'axios'
import useTeams from '@/hooks/useTeams'
import { validateFirstTeam, validateSecondTeam } from './validation'
import { GameCreationSchema } from '@/types/games'

export default function PlayedGameCreationForm() {
  const { isLoading, data } = useTeams()

  const form = useForm({
    initialValues: {
      firstTeamId: null,
      secondTeamId: null,
      firstTeamGoals: 0,
      secondTeamGoals: 0,
    },
    validate: {
      firstTeamId: validateFirstTeam,
      secondTeamId: validateSecondTeam,
      firstTeamGoals: (value) =>
        value < 0 ? 'Value cannot be negative' : null,
      secondTeamGoals: (value) =>
        value < 0 ? 'Value cannot be negative' : null,
    },
  })

  const submit = (values: any) => {
    const data: GameCreationSchema = {
      first_team_id: parseInt(values.firstTeamId, 10),
      second_team_id: parseInt(values.secondTeamId, 10),
      first_team_goals: parseInt(values.firstTeamGoals, 10),
      second_team_goals: parseInt(values.secondTeamGoals, 10),
    }
    axios.post('http://localhost:8000/games', data).then((response) => {
      if (response.status === 200) {
        notifications.show({
          message: 'Success! Your team has been created.',
        })
        form.reset()
      }
    })
  }

  if (isLoading) {
    return (
      <Center data-testid="loader">
        <Loader color="blue" />
      </Center>
    )
  }
  if (data) {
    const teamsData = data.map((team) => ({
      value: team.id.toString(),
      label: team.name,
    }))

    return (
      <>
        <form onSubmit={form.onSubmit(submit)}>
          <SimpleGrid cols={2}>
            <Select
              data-testid="first-team-select"
              label="First Team"
              name="firstTeamId"
              placeholder="Pick a team"
              data={teamsData}
              required={true}
              {...form.getInputProps('firstTeamId')}
            />
            <NumberInput
              data-testid="first-team-goals-input"
              label="First Team Goals"
              defaultValue={0}
              required={true}
              name="firstTeamGoals"
              {...form.getInputProps('firstTeamGoals')}
            />
            <Select
              data-testid="second-team-select"
              label="Second Team"
              name="secondTeamId"
              placeholder="Pick a team"
              data={teamsData}
              required={true}
              {...form.getInputProps('secondTeamId')}
            />
            <NumberInput
              data-testid="second-team-goals-input"
              label="Second Team Goals"
              defaultValue={0}
              required={true}
              name="secondTeamGoals"
              {...form.getInputProps('secondTeamGoals')}
            />
          </SimpleGrid>
          <Group justify="center" mt="md">
            <Button type="submit" size="md" data-testid="create-game-button">
              Create Game
            </Button>
          </Group>
        </form>
      </>
    )
  }

  return <div>Teams could not be loaded</div>
}
